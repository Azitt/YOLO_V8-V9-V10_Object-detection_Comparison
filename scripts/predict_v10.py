## install before running##################
#pip install huggingface_hub
# pip install git+https://github.com/THU-MIG/yolov10.git
import os
os.environ["CUDA_VISIBLE_DEVICES"] ="3"
from ultralytics import YOLOv10

# # Load a pretrained YOLOv8n model
model = YOLOv10("./weights/best.pt")

model.predict(source="./video_inference2.mp4", save=True, conf=0.5,device =3)