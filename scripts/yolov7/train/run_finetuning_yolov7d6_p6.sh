#!/bin/bash

num_sims=5  # Number of experiments

for i in $(seq 1 $num_sims)
do
    echo "Simulation: $i"
    echo "--------------"
    python train_aux.py  \
        --epochs 200  \
        --workers 8  \
        --device 0  \
        --batch-size 4  \
        --data data/welding_data_v7.yaml  \
        --img 1280  \
        --cfg cfg/training/yolov7-d6_welding.yaml  \
        --weights training_yolov7_p6/yolov7d6'_'$i/weights/best.pt  \
        --name yolov7d6'_'$i  \
        --project finetuning_yolov7_p6  \
        --hyp data/hyp.scratch.p6-ft.yaml  \
        --freeze 0
done

