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
        --data welding_data.yaml  \
        --weights yolov5l.pt  \
        --project training_yolov5_p5  \
        --name yolov5l'_'$i  \
        --cache  \
        --freeze 10  \
	--seed $i  \
        --hyp data/hyps/hyp.scratch-low.yaml
done
