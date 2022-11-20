#!/bin/bash

RUN_ID=${1:-"lambda"}

export INPUT_DIR="/home/ubuntu/ml/neurips2022/person/${RUN_ID}/input"

mkdir -p $INPUT_DIR

echo "Resize images in ${INPUT_DIR}: "
python compress.py $INPUT_DIR

echo "Repare Jupyter notebook"

cp "helper.py" "/home/ubuntu/ml/neurips2022/person/${RUN_ID}"
cp "test.ipynb" "/home/ubuntu/ml/neurips2022/person/${RUN_ID}/test_${RUN_ID}.ipynb"
sed -i "s/chuanli/${RUN_ID}/g" "/home/ubuntu/ml/neurips2022/person/${RUN_ID}/test_${RUN_ID}.ipynb"
