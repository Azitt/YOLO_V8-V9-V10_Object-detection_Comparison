

from ultralytics import YOLO
import os
os.environ["CUDA_VISIBLE_DEVICES"] ="3" 

# Load a COCO-pretrained YOLOv9c model
model = YOLO("./yolov9c.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="./data.yaml", epochs=100, imgsz=640, device=3, workers=2,batch=4)