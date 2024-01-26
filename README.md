# Welding Defect Detection with YOLO algorithms on a Limited Dataset: A Comparative Study

# Environment installations

```
mkdir welding
cd welding
```

For the installation [Anaconda](https://www.anaconda.com/download) is used on Ubuntu 22.04.
## YOLOv5
In the base environment:
```
conda create --name yolov5 python=3.8 -y
conda activate yolov5
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

## YOLOv7
In the base environment:
```
conda create --name yolov7 python=3.8 -y
conda activate yolov7
git clone https://github.com/WongKinYiu/yolov7.git
cd yolov7
pip install -r requirements.txt
```

## YOLOv6 and YOLOv8
In the base environment
```
conda create --name yolov8 python=3.8 -y
conda activate yolov8
git clone https://github.com/ultralytics/ultralytics yolov8
cd yolov8
pip install -e .
```

# Dataset preparations
The full dataset is available at [here](https://drive.google.com/file/d/1GrHhiCdmRnXbXEyWrLGfGGD0eS3YwDUb/view?usp=sharing).

## YOLOv5
Download, unzip the `welding_images.zip` file from the link above
which contains the images and the annotations and copy the `images` directory from it
into `yolov5/data/` and replace the original `images` directory.
Create a `labels` directory and copy the `.txt` files from `images` to in:
```
cp images/*.txt labels/.
```

Copy the `yolov5_files/autosplit_*.txt` files to the `yolov5/data` directory.

Copy the `yolov5_files/welding_data.yaml` file to the `yolov5` directory.

Copy the `yolov5_files/hyp*.yaml` files to `yolov5/data/hyps` directory.

Example training:
-----------------
```
python train.py --cos-lr --img 640 --batch 32 --epochs 200 --data welding_data.yaml --weights yolov5n.pt --project defects --name model_5n_dec4 --cache --freeze 10 
```

## YOLOv7
Copy the data directory from `yolov5` to `yolov7`:
```
cp -avr yolov5/data/images yolov7/data/images
cp yolov5/data/autosplit*.txt yolov7/data/.
```
Copy the `yolov7_files/split_datasplit.py` function to `yolov7/data` and call it by :
```
python split_dataset.py --folder images --dest images_welding
```

Copy the `yolov7_files/welding_data_v7.yaml` file to the `yolov7/data` directory.
Copy the `yolov7.yaml` and `yolov7*.yaml` configuration files from the `yolov7_files` directory to the `yolov7/cfg/training` directory.
Copy the `yolov7/utils/loss.py` file to `yolov7/utils/loss.py`.
Copy the `hyp*.yaml` ciles to `yolov7/data`.

Download from [here](https://github.com/pHidayatullah/yolov7/tree/main) 
the `yolov7*_training.pt` files and copy them to the `yolov7` directory.

Copy the `yolov7_files/train_aux.py` file and copy to `yolov7` directory. There has been added a `--freeze` argument to the parser.

Example training:
-----------------
```
python train.py --epochs 50 --workers 8 --device 0 --batch-size 4 --data data/welding_data_v7.yaml --img 640 --cfg cfg/training/yolov7_welding.yaml --weights 'yolov7_training.pt' --name yolov7-w1 --hyp data/hyp.scratch.custom.yaml --project defects --freeze 50
```


 
