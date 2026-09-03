from ultralytics import YOLO

# This pulls a tiny, pre-trained model and prints its architecture
model = YOLO('yolov8n.pt') 
model.info()