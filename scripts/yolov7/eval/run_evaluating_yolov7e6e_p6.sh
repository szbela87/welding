#!/bin/bash

num_sims=5  # Number of experiments

for i in $(seq 1 $num_sims)
do
    echo "Simulation: $i"
    echo "--------------"
    python test.py  \
        --device 0  \
	--task test  \
        --batch-size 4  \
        --data data/welding_data_v7.yaml  \
        --img 1280  \
        --weights finetuning_yolov7_p6/yolov7e6e'_'$i/weights/best.pt  \
        --name yolov7e6e'_'$i  \
        --project testing_yolov7_p6  
done

