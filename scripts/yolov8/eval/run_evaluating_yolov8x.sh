#!/bin/bash

# Number of simulations
num_sims=5

for i in $(seq 1 $num_sims)
do
    echo "Simulation id: $i"
    echo "-----------------"
    python eval.py  \
		--data './data/welding_data_v8.yaml'  \
		--weight finetuning_yolov8/yolov8x'_'$i/weights/best.pt  \
		--batch 8  \
		--imgsz 640  \
		--device 0  \
		--project 'testing_yolov8'  \
		--name yolov8x'_'$i  
done
