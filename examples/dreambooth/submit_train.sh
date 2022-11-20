#!/bin/bash

RUN_ID=${1:-"lambda"}
GPU_ID=${2:-"0"}

export MODEL_NAME="CompVis/stable-diffusion-v1-4"
export CLASS_DATA_DIR="/home/ubuntu/ml/neurips2022/class_data/set1"
export TOKEN="aabbccddeeffgg"

export INPUT_DIR="/home/ubuntu/ml/neurips2022/person/${RUN_ID}/input"
export PRED_DIR="/home/ubuntu/ml/neurips2022/person/${RUN_ID}/output"
export MODEL_DIR="/home/ubuntu/ml/neurips2022/person/${RUN_ID}/model"

mkdir -p $INPUT_DIR
mkdir -p $PRED_DIR
mkdir -p $MODEL_DIR
mkdir -p $CLASS_DATA_DIR

echo $RUN_ID
echo $INPUT_DIR
echo $PRED_DIR
echo $MODEL_DIR
echo $CLASS_DATA_DIR

python compress.py $INPUT_DIR

CUDA_VISIBLE_DEVICES=$GPU_ID python train_dreambooth.py   \
	--pretrained_model_name_or_path=$MODEL_NAME    \
	--instance_data_dir=$INPUT_DIR   \
	--train_text_encoder \
	--output_dir=$MODEL_DIR \
	--instance_prompt="a photo of aabbccddeeffgg person"   \
	--resolution=512   \
	--train_batch_size=2 \
	--gradient_accumulation_steps=1   \
	--lr_scheduler="constant"   \
	--lr_warmup_steps=0 \
	--learning_rate=1e-6 \
	--max_train_steps=1000 \
	--pred_path $PRED_DIR

echo "Job ${RUN_ID} is done, GPU ${GPU_ID} is free."
