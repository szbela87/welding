import argparse
from ultralytics import YOLO
from timeit import default_timer

def parse_args():
    parser = argparse.ArgumentParser(description="Train a YOLO model with specified arguments.")
    parser.add_argument('--data', type=str, default='./data/welding_data_v8.yaml', help='Dataset YAML file path')
    parser.add_argument('--weight', type=str, default='yolov8n.pt', help='Model for training/Model weights for fine tuning')
    parser.add_argument('--batch', type=int, default=8, help='Batch size')
    parser.add_argument('--imgsz', type=int, default=640, help='Image size')
    parser.add_argument('--seed', type=int, default=0, help='Random seed')
    parser.add_argument('--device', type=int, default=0, help='Device ID')
    parser.add_argument('--epochs', type=int, default=200, help='Number of epochs')
    parser.add_argument('--freeze', type=int, default=0, help='Freezing layers (for Yolov8 the backbone has 10 layers)')
    parser.add_argument('--project', type=str, default='alma', help='Project name')
    parser.add_argument('--name', type=str, default='yolov8n_test1', help='Name of the run')
    parser.add_argument('--optimizer', type=str, default='SGD', help='Optimizer type')
    parser.add_argument('--lr0', type=float, default=0.01, help='Initial learning rate')
    parser.add_argument('--lrf', type=float, default=0.1, help='Final learning rate')
    parser.add_argument('--warmup_epochs', type=float, default=3.0, help='Warmup epochs')
    parser.add_argument('--cos_lr',action='store_true',help='Use cosine LR scheduler')
    

    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    
    # Creating the YOLO model
    model = YOLO(args.weight)
    
    print(f"cos_lr: {args.cos_lr}")

    ts = default_timer()

    # Training
    model.train(
        data=args.data,
        batch=args.batch,
        imgsz=args.imgsz,
        device=args.device,
        epochs=args.epochs,
        project=args.project,
        name=args.name,
        seed=args.seed,
        optimizer=args.optimizer,
        lr0=args.lr0,
        lrf=args.lrf,
        warmup_epochs=args.warmup_epochs,
        freeze=args.freeze,
        cos_lr=args.cos_lr
    )

    te = default_timer()

    print(160*"-")
    print(f"TIME: {te-ts:4f}")

if __name__ == "__main__":
    main()
