from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# train the model
results = model.train(data="Data\config.yaml", epochs=300)