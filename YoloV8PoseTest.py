from ultralytics import YOLO

# Load a model
model = YOLO(r'/best.pt')  # load an official model
# model = YOLO('yolov8m-pose.pt')  # load an official model
# model = YOLO('path/to/best.pt')  # load a custom model

# Predict with the model
# results = model('https://ultralytics.com/images/bus.jpg')  # predict on an image

result = model(source=r"C:\PyCharm_project_final_year\Yolov8_yoga_pose\data_folder\images\train\Anjaneyasana\1 (27).jpg", show=True, conf=0.3, save=True)
# results = model(source=r"C:\Users\snehal\PycharmProjects\PoseEstimationTrainer\data\tadasan.mp4", show=True, conf=0.3, save=True)
# results = model(source=0, show=True, conf=0.3, save=True)

boxes = result.boxes  # Boxes object for bbox outputs
masks = result.masks  # Masks object for segmentation masks outputs
keypoints = result.keypoints  # Keypoints object for pose outputs
probs = result.probs  # Probs object for classification outputs