import os

from ultralytics import YOLO


model = YOLO('yolov8n-pose.pt')  # load a pretrained model (recommended for training)

model.train(data=r'C:\PyCharm_project_final_year\Yolov8_yoga_pose\config.yml', epochs=50, imgsz=640)