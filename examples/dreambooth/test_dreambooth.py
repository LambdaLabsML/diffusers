import os
import time
from pathlib import Path
import argparse

import torch

from diffusers import StableDiffusionPipeline
from helper import create_tests
from helper import dummy

# The flag below controls whether to allow TF32 on matmul. This flag defaults to False
# in PyTorch 1.12 and later.
if os.environ['USE_TF32'] == "on":
    torch.backends.cuda.matmul.allow_tf32 = True
    print("TF32 is on --------------------------------")
else:
    torch.backends.cuda.matmul.allow_tf32 = False
    print("TF32 is off --------------------------------")


def parse_args(input_args=None):
    parser = argparse.ArgumentParser(description="Simple example of a testing script.")
    parser.add_argument(
        "--pred_path",
        type=str,
        default=None,
        required=True,
        help="Path to save generate images.",
    )
    parser.add_argument(
        "--model_path",
        type=str,
        default=None,
        required=True,
        help="Path to model.",
    )
    parser.add_argument(
        "--token",
        type=str,
        default="aabbccddeeffgg",
        help="Special token.",
    )
    parser.add_argument(
        "--tests",
        type=str,
        default="all",
        help="list of test ids. default all uses all the test prompts",
    )
    parser.add_argument(
        "--num_pred_steps",
        type=int,
        default=75,
        help="Number of steps for inference.",
    )
    parser.add_argument(
        "--guide",
        type=float,
        default=7.5,
        help="Guide power.",
    )
    parser.add_argument(
        "--num_preds",
        type=int,
        default=1,
        help="Number of predictions for each prompt.",
    )
    args = parser.parse_args()
    
    return args

def main():
    args = parse_args()
    
    pipe = StableDiffusionPipeline.from_pretrained(args.model_path, torch_dtype=torch.float16).to("cuda")
    pipe.safety_checker = dummy

    Path(args.pred_path).mkdir(parents=True, exist_ok=True)
    tests = create_tests(args.tests, args.token, args.num_pred_steps, args.guide)
    
    for i in range(args.num_preds):
        for key in tests:
            image = pipe(tests[key][0], num_inference_steps=tests[key][1], guidance_scale=tests[key][2]).images[0]
            timestr = time.strftime("%Y%m%d-%H%M%S")
            image.save(args.pred_path + "/" + key + "-" + tests[key][3] + "-" + timestr + "-" + ".png")
        
if __name__ == "__main__":
    main()





