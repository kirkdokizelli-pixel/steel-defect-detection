from ultralytics import YOLO

model = YOLO('yolov8s.pt')
model.train(data='data.yaml', epochs=100, imgsz=640, batch=16, patience=20)
