#Using YoloV8
import sys
from PIL import Image
from ultralytics import YOLO
import cv2
import argparse
import supervision as sv

def parseArgs()->argparse.Namespace:
    parser=argparse.ArgumentParser(description="YoloV8Cam")
    parser.add_argument(
        "--webcam-resolution", 
        default=[1280,720],
        nargs=2, 
        type=int
    )

    args=parser.parse_args()
    return args

def liveCamera(model):
    #get camera resolution
    args=parseArgs()
    frameWidth, frameHeight=args.webcam_resolution

    #open camera
    try:
        camera=cv2.VideoCapture(0)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT,frameHeight)
        camera.set(cv2.CAP_PROP_FRAME_WIDTH,frameWidth)
    except:
        sys.exit("Camera Not Connected")
 
    #create bounding boxes to add around detected objects
    boxAnnotator= sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )
    #Anything Below Threshold will not be marked
    threshold=0.5   

    while True:
        #retrive a frame from the image
        ret, frame=camera.read()
    
        #run the frame through the yolov8 model
        results=model(frame,conf=threshold)[0]

        #draw boxes around detected objects
        detection=sv.Detections.from_yolov8(results)
        #get the labels and confidence value from the detection
        labels=[
            f"{model.names[class_id]} {confidence:0.2f}"
            for _,confidence,class_id, _
            in detection
        ]
        #Add the box around detected object
        frame=boxAnnotator.annotate(scene=frame, detections=detection, labels=labels)

        #display frame to user
        cv2.imshow("YoloMethod",frame)

        #Escape key will close the window
        if(cv2.waitKey(30)==27):
            break


def stillImage(model,path):
   
    result=model(path, conf=0.5)
    result=result[0]

    print(len(result.boxes))

    for box in result.boxes:
        label=result.names[box.cls[0].item()]
        cords=[round(x) for x in box.xyxy[0].tolist()]
        confidence=round(box.conf[0].item(),2)
        print("Object Type: ",label)
        print("Coordinates: ",cords)
        print("Confidence: ",confidence)
        print("-------------------------")
    
    Image.fromarray(result.plot( )[:,:,::-1]).show()

    

def main():
    #Load the YOLO model
    modelPath="runs/detect/train/weights/last.pt"
    model=YOLO(modelPath)
    
    imagePath1="Data/images/train/20230915_122551.jpg"
    imagePath2="Data/images/train/20230915_124542.jpg"
    imagePath3="Data/images/train/20230915_124629.jpg"

    stillImage(model,imagePath3)
    #liveCamera(model)
    

if __name__ == "__main__":
    main()
