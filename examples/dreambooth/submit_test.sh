#!/bin/bash

RUN_ID=${1:-"lambda"}
GPU_ID=${2:-"0"}
TF32=${3:-"off"}
NUM_PRED=${4:-"1"}
TESTS=${5:-"all"}

export MODEL_NAME="CompVis/stable-diffusion-v1-4"
export CLASS_DATA_DIR="/home/ubuntu/ml/neurips2022/class_data/set1"
export TOKEN="aabbccddeeffgg"

export INPUT_DIR="/home/ubuntu/ml/neurips2022/person/${RUN_ID}/input"
export PRED_DIR="/home/ubuntu/ml/neurips2022/person/${RUN_ID}/output"
export MODEL_DIR="/home/ubuntu/ml/neurips2022/person/${RUN_ID}/model"
export USE_TF32=$TF32

mkdir -p $INPUT_DIR
mkdir -p $PRED_DIR
mkdir -p $MODEL_DIR
mkdir -p $CLASS_DATA_DIR

echo $RUN_ID
echo $INPUT_DIR
echo $PRED_DIR
echo $MODEL_DIR
echo $CLASS_DATA_DIR


CUDA_VISIBLE_DEVICES=$GPU_ID python test_dreambooth.py \
	--model_path $MODEL_DIR \
	--pred_path $PRED_DIR \
	--tests $TESTS \
	--num_preds $NUM_PRED


echo "Job ${RUN_ID} is done, GPU ${GPU_ID} is free."
