from ultralytics import YOLO

model = YOLO('yolov8n.pt')

results = model.train(data='Detecting diseases.v6i.yolov8/data.yaml', epochs=10, imgsz=640)