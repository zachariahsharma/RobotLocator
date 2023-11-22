from ultralytics import YOLO
model = YOLO('yolov8n.pt')
model.tune(data='./Robot-Locator-7/data.yaml', epochs=30, iterations=300,
           optimizer='AdamW', plots=False, save=False, val=False)
new_model = YOLO('./runs/tune/weights/best.pt')
new_model.train(epochs=200)
new_model.export("./RobotLocatoer.pt")
