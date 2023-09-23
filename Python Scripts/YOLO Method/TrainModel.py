from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# train the model
results = model.train(data="A:\Code\Visual Studio Code Projects\Python\Digital-Twin-CS_Capstone\Python Scripts\YOLO Method\Data\config.yaml", epochs=150)  # Change to relative path