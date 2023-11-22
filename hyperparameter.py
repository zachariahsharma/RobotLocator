from ultralytics import YOLO
# model = YOLO('yolov8n.pt')
# model.tune(data='./Robot-Locator-7/data.yaml', epochs=20, iterations=100,
#            optimizer='AdamW', plots=False, save=False, val=False, device=0, resume=True)
new_model = YOLO('/RobotLocator/runs/detect/tune2/weights/best.pt')
new_model.train("/RobotLocator/Robot-Locator-7/data.yaml",
                epochs=200, lr0=0.0055, lrf=0.01522, momentum=0.82781, weight_decay=0.00034, warmup_epochs=2.78171, warmup_momentum=0.95, box=5.53366, cls=0.57088, dfl=1.49239, hsv_h=0.01744, hsv_s=0.87224, hsv_v=0.33701, degrees=0.0, translate=0.10377, scale=0.51213, shear=0.0, perspective=0.0, flipud=0.0, fliplr=0.40329, mosaic=0.53419, mixup=0.0, copy_paste=0.0, device=0)
new_model.export()
