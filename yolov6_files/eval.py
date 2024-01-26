import argparse
from ultralytics import YOLO

def parse_args():
    parser = argparse.ArgumentParser(description="Train a YOLO model with specified arguments.")
    parser.add_argument('--data', type=str, default='./data/welding_data_v8.yaml', help='Dataset YAML file path')
    parser.add_argument('--weight', type=str, default='yolov8n.pt', help='Model for training/Model weights for fine tuning')
    parser.add_argument('--batch', type=int, default=8, help='Batch size')
    parser.add_argument('--imgsz', type=int, default=640, help='Image size')
    parser.add_argument('--device', type=int, default=0, help='Device ID')
    parser.add_argument('--project', type=str, default='alma', help='Project name')
    parser.add_argument('--name', type=str, default='yolov8n_test1', help='Name of the run')    
    parser.add_argument('--split', type=str, default='test', help='test/val')    

    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    
    # Creating the YOLO model
    model = YOLO(args.weight)
    
    # Training
    metrics = model.val(
        data=args.data,
        batch=args.batch,
        imgsz=args.imgsz,
        device=args.device,
        project=args.project,
        name=args.name,
        split=args.split
    )
    
    print(160*"*")
    print(f"FITNESS: {metrics.fitness:.4f}")

if __name__ == "__main__":
    main()
