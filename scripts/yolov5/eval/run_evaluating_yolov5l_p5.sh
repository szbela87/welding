#!/bin/bash

num_sims=5  # Number of experiments

for i in $(seq 1 $num_sims)
do
    echo "Simulation: $i"
    echo "--------------"
    python val.py  \
        --img 640  \
        --batch 8  \
        --data welding_data.yaml  \
        --weights finetuning_yolov5_p5/yolov5l'_'$i/weights/best.pt  \
        --project testing_yolov5_p5  \
        --name yolov5l'_'$i  
done
