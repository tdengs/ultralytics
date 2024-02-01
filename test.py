from ultralytics.models.yolo.detect import DetectionTrainer

args = dict(model='C:\\Users\\Deng Shyang Teh\\OneDrive\\Desktop\\CS degree\\FYP\\ultralytics\\ultralytics\\cfg\\models\\v8\\my-yolov8n.yaml', data='coco8.yaml', epochs=3)
trainer = DetectionTrainer(overrides=args)
trainer.train()