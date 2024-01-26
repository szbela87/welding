#!/bin/bash

# Number of simulations
num_sims=5

for i in $(seq 1 $num_sims)
do
    echo "Simulation id: $i"
    echo "-----------------"
    python train.py  \
		--data './data/welding_data_v8.yaml'  \
		--weight training_yolov8/yolov8x'_'$i/weights/best.pt  \
		--batch 8  \
		--imgsz 640  \
		--device 0  \
		--epochs 200  \
		--seed $(($i+5))  \
		--project 'finetuning_yolov8'  \
		--name yolov8x'_'$i  \
		--optimizer 'SGD'  \
		--lr0 0.001  \
		--lrf 0.1  \
		--warmup_epochs 0.0  \
		--cos_lr
done
