#!/bin/bash

# Number of simulations
num_sims=5

if [ ! -d "./results" ]; then
    mkdir ./results
fi

for i in $(seq 1 $num_sims)
do
    echo "Simulation id: $i"
    echo "-----------------"
    python eval.py  \
		--data './data/welding_data_v6.yaml'  \
		--weight finetuning_yolov6/yolov6n'_'$i/weights/best.pt  \
		--batch 8  \
		--imgsz 640  \
		--device 0  \
		--project 'testing_yolov6'  \
		--name yolov6n'_'$i >>results/yolov6n'_'results.txt
done
