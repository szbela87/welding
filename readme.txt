




mkdir welding
cd welding

# Environment installations

## yolov5
### from the base environment
conda create --name yolov5 python=3.8 -y
conda activate yolov5
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt

## yolov7
### from the base environment
conda create --name yolov7 python=3.8 -y
conda activate yolov7
git clone https://github.com/WongKinYiu/yolov7.git
cd yolov7
pip install -r requirements.txt

## yolov8
### from the base environment
conda create --name yolov8 python=3.8 -y
conda activate yolov8
git clone https://github.com/ultralytics/ultralytics yolov8
cd yolov8
pip install -e .

# dataset preparations
the full dataset is available at: 

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

Example training:
-----------------
python train.py --cos-lr --img 640 --batch 32 --epochs 200 --data welding_data_v5.yaml --weights yolov5n.pt --project defects --name model_5n_dec4 --cache --freeze 10 

## yolov7
Copy the data directory from `yolov5` to `yolov7`:
cp -avr yolov5/data/images yolov7/data/images
cp yolov5/data/autosplit*.txt yolov7/data/.
Download the `split_datasplit.py` function 
and call it by :
`python split_dataset.py --folder images --dest images_welding`

Download the welding_data_v7.yaml file from the Google Drive link and copy to the `yolov7/data` directory.
Download the `.yaml` configuration files from the `v7_cfg` directory in the Google Drive link and copy them to the `yolov7/cfg/training` directory.
Download the `yolov7/utils/loss.py` file from the Google Drive link and rewrite the `yolov7/utils/loss.py'. Some bugs are fixed.

Download from https://github.com/pHidayatullah/yolov7/tree/main
the `yolov7*_training.pt` files and copy them to the `yolov7` directory.
They are also available at the Google Drive link in the directory `v7_tl_models`.

Download `train_aux.py` file and copy to `yolov7` directory. There has been added a `--freeze` argument to the parser. This was a bug.

Example training:
-----------------
python train.py --epochs 50 --workers 8 --device 0 --batch-size 4 --data data/welding_data_v7.yaml --img 640 --cfg cfg/training/yolov7_welding.yaml --weights 'yolov7_training.pt' --name yolov7-w1 --hyp data/hyp.scratch.custom.yaml --project defects --freeze 50

## yolov8
Copy the `data` directory from `yolov7` to `yolov8`:
cp -avr yolov7/data yolov8/data

Modify the second line if the file `/home/$user/.config/Ultralytics/settings.yaml` to `yolov8` and the erase `dataset` from the end of line.

Download the `welding_data_v8.yaml` file from the Google Drive link and copy to the `yolov8/data` directory.

Example:
datasets_dir: /home/$username/Documents/programs/welding/yolov8
weights_dir: weights
runs_dir: runs

Example training
----------------
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model = YOLO("yolov8m.pt")
model.train(data="./data/welding_data_v8.yaml",batch=8,imgsz=640,device=0,epochs=100,name="detect/yolov8n_1")
model.train(data="./data/welding_data_v8.yaml",batch=8,imgsz=640,device=0,epochs=200,name="yolov8n_test1",optimizer="SGD",lr0=0.01,lrf=0.1)
model.train(data="./data/welding_data_v8.yaml",batch=8,imgsz=640,device=0,epochs=50,name="test1/yolov8n_auto2",freeze=10)
model = YOLO("./runs/detect/test1/yolov8n_auto2/weights/best.pt")
metrics = model.val(data="./data/welding_data.yaml",split="test")

Fine tuning
-----------
model.train(data="./data/welding_data_v8.yaml",batch=8,imgsz=640,device=0,epochs=50,name="test1/yolov8n_auto_new",lr0=0.001,lrf=0.1,warmup_epochs=0.0)
model.train(data="./data/welding_data_v8.yaml",batch=8,imgsz=640,device=0,epochs=200,name="test1/yolov8n_auto_new",optimizer="SGD",lr0=0.01,lrf=0.1,warmup_epochs=0.0)

Evaluating
----------
