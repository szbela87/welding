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
        --weights yolov5m6.pt  \
        --project training_yolov5_p6  \
        --name yolov5m6'_'$i  \
        --cache  \
        --freeze 10  \
        --hyp data/hyps/hyp.scratch-high.yaml
done
