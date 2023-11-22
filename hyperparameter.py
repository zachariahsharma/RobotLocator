from ultralytics import YOLO
# model = YOLO('yolov8n.pt')
# model.tune(data='./Robot-Locator-7/data.yaml', epochs=20, iterations=100,
#            optimizer='AdamW', plots=False, save=False, val=False, device=0, resume=True)
new_model = YOLO('/RobotLocator/runs/detect/tune2/weights/best.pt')
new_model.train("/RobotLocator/Robot-Locator-7/data.yaml",
                epochs=200, device=0)
new_model.export("/RobotLocatoer.pt")
