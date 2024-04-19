from PIL import Image
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
results = model('data/bb1.jpg')  # results list
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save('resultBB.jpg')  # save image