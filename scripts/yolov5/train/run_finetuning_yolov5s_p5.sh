#!/bin/bash

num_sims=5  # Number of experiments

for i in $(seq 1 $num_sims)
do
    echo "Simulation: $i"
    echo "--------------"
    python train.py  \
        --cos-lr  \
        --img 640  \
        --batch 8  \
        --epochs 200  \
	--seed $(($i+5))  \
        --data welding_data.yaml  \
        --weights training_yolov5_p5/yolov5s'_'$i/weights/best.pt  \
        --project finetuning_yolov5_p5  \
        --name yolov5s'_'$i  \
        --cache  \
        --hyp data/hyps/hyp.scratch-low-ft.yaml
done
