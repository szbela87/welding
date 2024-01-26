#!/bin/bash

# Number of simulations
num_sims=5

for i in $(seq 1 $num_sims)
do
    echo "Simulation id: $i"
    echo "-----------------"
    python train.py  \
		--data './data/welding_data_v6.yaml'  \
		--weight 'yolov6s.yaml'  \
		--batch 8  \
		--imgsz 640  \
		--device 0  \
		--epochs 200  \
		--seed $i  \
		--project 'training_yolov6'  \
		--name yolov6s'_'$i  \
		--optimizer 'SGD'  \
		--lr0 0.01  \
		--lrf 0.1  \
		--warmup_epochs 3.0  \
		--freeze 11  \
		--cos_lr
done
