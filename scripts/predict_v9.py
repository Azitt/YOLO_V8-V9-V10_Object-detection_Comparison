from ultralytics import YOLO

# # Load a pretrained YOLOv8m model
model = YOLO("./weights/best.pt")

model.predict(source="./video_inference2.mp4", save=True, conf=0.5,device =3)