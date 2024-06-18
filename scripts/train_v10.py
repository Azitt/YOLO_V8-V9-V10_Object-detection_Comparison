# pip install git+https://github.com/THU-MIG/yolov10.git
# pip install safetensors
## train###################
from ultralytics import YOLOv10
import torch
import os
os.environ["CUDA_VISIBLE_DEVICES"] ="3"

model = YOLOv10.from_pretrained('jameslahm/yolov10m')
# Training
model.train(data="./data.yaml", epochs=100, imgsz=640, device=3, workers=1,batch=4)
