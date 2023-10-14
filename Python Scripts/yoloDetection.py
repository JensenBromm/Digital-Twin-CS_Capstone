#Using YoloV8
import sys
from ultralytics import YOLO
import cv2
import argparse
import supervision as sv  #MAKE SURE THIS IS VERSION 0.3.0  (pip install supervision==0.3.0)

#Define Global variables
#Load the YOLO model
modelPath="runs/detect/train/weights/last.pt"
model=YOLO(modelPath)

#create bounding boxes to add around detected objects
boxAnnotator= sv.BoxAnnotator(
    thickness=2,
    text_thickness=1,
    text_scale=0.25
)
#Anything Below Threshold will not be marked
threshold=0.6


#Get the user input for camera resolution from command line
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

#Object detection using webcam footage
def webcam():
    #get camera resolution
    args=parseArgs()
    frameWidth, frameHeight=args.webcam_resolution

    #open camera
    try:
        camera=cv2.VideoCapture(0)
        #Make sure that the camera is connected and can be read from
        if(camera.read()[0]==False):
            raise Exception
        
        #Set the resolution of the camera (Passed in by CMD Line or 1280x720)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT,frameHeight)
        camera.set(cv2.CAP_PROP_FRAME_WIDTH,frameWidth)
    except:
        #Stop the program since no camera is connected
        sys.exit("Camera Not Connected")

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

    camera.release()
    cv2.destroyAllWindows()

#Connect to Camera over RTSP Stream
def liveCamera(ip):
     #get camera resolution
    args=parseArgs()
    frameWidth, frameHeight=args.webcam_resolution

    #open camera
    try:
        camera=cv2.VideoCapture(ip)
        #Make sure that the camera is connected and can be read from
        if(camera.isOpened()==False):
            raise Exception
        
        #Set the resolution of the camera (Passed in by CMD Line or 1280x720)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT,frameHeight)
        camera.set(cv2.CAP_PROP_FRAME_WIDTH,frameWidth)
    except:
        #Stop the program since no camera is connected
        sys.exit("Cannot connect to camera")
 
    #create bounding boxes to add around detected objects
    boxAnnotator= sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )
       

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

    camera.release()
    cv2.destroyAllWindows()

#object detection using a jpg image
def stillImage(path):
    frame=cv2.imread(path)

    #Predict what objects are in the image
    results=model(frame, conf=threshold)[0] #CONF means that is has to be >50% sure that the object is there
    detections = sv.Detections.from_yolov8(results)

    labels = [f"{model.names[class_id]} {confidence:0.2f}" for _, confidence, class_id, _ in detections]
    frame = boxAnnotator.annotate(scene=frame, detections=detections, labels=labels)

    #Open the image
    sv.show_frame_in_notebook(frame, (16, 16))

#Object Detection via Pre-Recorded Video
def video(path):
    if(len(path)==0):
        sys.exit("Path Can Not be blank")
    
    #open the video
    try:
        camera=cv2.VideoCapture(path)
        if(camera.isOpened()==False):
            raise Exception
       
    except:
        #Stop the program since no path was provided is connected
        sys.exit("Error: Video could not be opened")


    while True:
        #retrive a frame from the image
        ret, frame=camera.read()
    
        if ret==True:
           
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

            for box in detection:
                print()

            #Escape key will close the window
            if(cv2.waitKey(30)==27):
                break
        else:
            break

    camera.release()
    cv2.destroyAllWindows()

#Call methods and link to YOLO model
def main():
    
    imagePath1="Data/images/train/20230915_122551.jpg" #Upclose Robot
    imagePath2="Data/images/train/Stream1 - frame at 0m1s.jpg" #Starting Lineup Stream1
    imagePath3="Data/images/train/Stream1 - frame at 8m0s.jpg" #Robots with Shelves
    testPath="output_image.jpg"

    videoPath="Videos/stream1.mp4"

    #Can only connect to security camera while on GSU campus
    cameraIP="rtsp://141.165.40.33/stream1"



    stillImage(imagePath3)
    #webcam()
    #liveCamera(cameraIP)
    #video(videoPath)
    

if __name__ == "__main__":
    main()
