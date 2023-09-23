#Using YoloV8
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
    camera=cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT,frameHeight)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH,frameWidth)

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


def main():
    #Load the YOLO model
    modelPath="runs/detect/train/weights/last.pt"
    model=YOLO(modelPath)

    liveCamera(model)

    

if __name__ == "__main__":
    main()
