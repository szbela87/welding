# Welding Defect Detection with YOLO algorithms on a Limited Dataset: A Comparative Study

# Environment installations

`mkdir welding
cd welding`

## YOLOv5
In the base environment:
`conda create --name yolov5 python=3.8 -y
conda activate yolov5
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt`

## YOLOv7
In the base environment:
`conda create --name yolov7 python=3.8 -y
conda activate yolov7
git clone https://github.com/WongKinYiu/yolov7.git
cd yolov7
pip install -r requirements.txt`

## YOLOv8
In the base environment
`conda create --name yolov8 python=3.8 -y
conda activate yolov8
git clone https://github.com/ultralytics/ultralytics yolov8
cd yolov8
pip install -e .`

# Dataset preparations
the full dataset is available at [here](https://drive.google.com/file/d/1GrHhiCdmRnXbXEyWrLGfGGD0eS3YwDUb/view?usp=sharing).

## yolov5
Download, unzip the `welding_images.zip` file
which contains the images and the annotations and copy the `images` directory from it
into `yolov5/data/` and replace the original `images` directory.
Create a `labels` directory and copy the `.txt` files from `images` to in:
cp images/*.txt labels/.

Also download the `autosplit_train.txt`, `autosplit_val.txt` and `autosplit_text.txt` files
from the google drive link above. Copy them to the `yolov5/data` directory.

/*
These are got from the following commands and they will be place in the `data` directory:
cd yolov5
from utils.dataloaders import autosplit
autosplit(path="data/images",weights=(0.7,0.2,0.1))
*/

Download the welding_data_v5.yaml file from the Google Drive link and copy to the `yolov5` directory.
 
