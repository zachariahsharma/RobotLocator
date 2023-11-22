from ultralytics import YOLO
# model = YOLO('yolov8n.pt')
# model.tune(data='./Robot-Locator-7/data.yaml', epochs=20, iterations=100,
#            optimizer='AdamW', plots=False, save=False, val=False, device=0, resume=True)
new_model = YOLO('/RobotLocator/runs/detect/tune2/weights/best.pt')
new_model.train("/RobotLocator/Robot-Locator-7/data.yaml",
                epochs=200, device=0)
new_model.export()
# lr0=0.0055, lrf=0.01522, momentum=0.82781, weight_decay=0.00034, warmup_epochs=2.78171, warmup_momentum=0.95, box=5.53366, cls=0.57088, dfl=1.49239,
