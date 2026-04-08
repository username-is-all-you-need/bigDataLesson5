"""
from ultralytics import YOLO
yolo = YOLO("./weights/yolov8n.pt","detect")
result = yolo(source="./ultralytics/assets/bus.jpg",save=False)

"""

from ultralytics import YOLO
model = YOLO('./weights/yolov8n.pt') #train the model
model.train(data='BVN_dataset.yaml',workers=0,epochs=50,batch=16)