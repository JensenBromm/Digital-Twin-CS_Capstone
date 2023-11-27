from yoloDetection import stillImage
from ultralytics import YOLO
import pytest

@pytest.fixture
def yolo_model():
    model_path = "runs/detect/train3/weights/best.pt"
    return YOLO(model_path)

@pytest.mark.order1
def test_all_robots(yolo_model): # This takes in a picture of each robot in the starting position
    
    names=yolo_model.names
    flag=True
    results=stillImage("Data/images/train/TopDown - frame at 0m0s.jpg")

    if len(results) !=4: # Make sure all 4 robots are detected
        flag=False
    else:
        classIDs=results.boxes.cls.tolist()
        for  i in range(len(classIDs)):
           name=names[classIDs[i]]
           if name != "AMR Robot": # Make sure that all detections are AMR Robots
                flag=False
                break
    
    assert flag is True

@pytest.mark.order2
def test_all_robots_mix(yolo_model): # Two Robots alone and Two Robots with shelfs
    names=yolo_model.names
    flag=True
    results=stillImage("Data/images/train/TopDown - frame at 1m19s.jpg")
    if len(results) != 4:  # Make sure all 4 robots are detected
        flag = False
    else:
        class_ids = results.boxes.cls.tolist()
    
        count_amr_robots = 0
        count_amr_with_shelf = 0

        for i in range(len(class_ids)):
            name = names[class_ids[i]]
            print(names)

            if name == "AMR Robot":
                count_amr_robots += 1
            elif name == "AMR Robot With Shelf":
                count_amr_with_shelf += 1

    if count_amr_robots == 2 and count_amr_with_shelf == 2:
        flag = True
    else:
        flag = False

    assert flag is True

@pytest.mark.order3
def test_all_robots_with_shelf(yolo_model): # This takes in a picture of each robot with a shelf
    names=yolo_model.names
    flag=True
    results=stillImage("Data/images/train/TopDown - frame at 1m7s.jpg")

    if len(results) !=4: # Make sure all 4 robots are detected
        flag=False
    else:
        classIDs=results.boxes.cls.tolist()
        for  i in range(len(classIDs)):
           name=names[classIDs[i]]
           print(names)
           if name != "AMR Robot With Shelf": # Make sure that all detections are AMR Robots with shelfs
                flag=False
                break

    assert flag is True


def test_blank(yolo_model): # This takes in an empty room to confirm there are no detections
    names=yolo_model.names
    flag=True
    results=stillImage("Videos/testBlankImage.jpg")

    if len(results) !=0: # Make sure nothing is detected
        flag=False
    
    assert flag is True

