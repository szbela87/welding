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
		--weight finetuning_yolov6/yolov6s'_'$i/weights/best.pt  \
		--batch 8  \
		--imgsz 640  \
		--device 0  \
		--project 'testing_yolov6'  \
		--name yolov6s'_'$i >>results/yolov6s'_'results.txt
done
