from ultralytics import YOLO
import os
os.environ["CUDA_VISIBLE_DEVICES"] ="3" 

# Load a COCO-pretrained YOLOv8n model
model = YOLO("./yolov8m.pt")

# Display model information (optional)
model.info()

# Train the model for 100 epochs
results = model.train(data="./data.yaml", epochs=100, imgsz=640, device=3, workers=2,batch=4)