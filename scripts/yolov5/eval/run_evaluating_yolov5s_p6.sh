#!/bin/bash

num_sims=5  # Number of experiments

for i in $(seq 1 $num_sims)
do
    echo "Simulation: $i"
    echo "--------------"
    python val.py  \
        --img 1280  \
        --batch 4  \
        --data welding_data.yaml  \
        --weights finetuning_yolov5_p6/yolov5s6'_'$i/weights/best.pt  \
        --project testing_yolov5_p6  \
        --name yolov5s6'_'$i  
done
