from ultralytics import YOLO
from roboflow import Roboflow
rf = Roboflow(api_key="NqnxVxO7l5RPeQIST4xj")
project = rf.workspace("school-tzde2").project("robot-locator")
model = YOLO('yolov8n.pt')
model.tune(data='./Robot-Locator-7/data.yaml', epochs=30, iterations=300,
           optimizer='AdamW', plots=False, save=False, val=False)
new_model = YOLO('./runs/tune/weights/best.pt')
new_model.train(epochs=200)
new_model.export("./RobotLocatoer.pt")
version = project.version(7)
version.deploy("model-type", "./RobotLocatoer.pt")
