#!/bin/bash

num_sims=5  # Number of experiments

for i in $(seq 1 $num_sims)
do
    echo "Simulation: $i"
    echo "--------------"
    python train.py  \
        --epochs 200  \
        --workers 8  \
        --device 0  \
        --batch-size 8  \
        --data data/welding_data_v7.yaml  \
        --img 640  \
        --cfg cfg/training/yolov7x_welding.yaml  \
        --weights training_yolov7_p5/yolov7x'_'$i/weights/best.pt  \
        --name yolov7x'_'$i  \
        --project finetuning_yolov7_p5  \
        --hyp data/hyp.scratch.custom-ft.yaml  \
        --freeze 0
done

