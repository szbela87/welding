#!/bin/bash

num_sims=5  # Number of experiments

for i in $(seq 1 $num_sims)
do
    echo "Simulation: $i"
    echo "--------------"
    python train.py  \
        --cos-lr  \
        --img 1280  \
        --batch 4  \
        --epochs 200  \
        --data welding_data.yaml  \
        --weights training_yolov5_p6/yolov5x6'_'$i/weights/best.pt  \
        --project finetuning_yolov5_p6  \
        --name yolov5x6'_'$i  \
        --cache  \
        --hyp data/hyps/hyp.scratch-high-ft.yaml
done
