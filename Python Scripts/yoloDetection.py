#Using YoloV8
import sys
from PIL import Image
from ultralytics import YOLO
import cv2
import argparse
import supervision as sv

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
def liveCamera(model):
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

    camera.release()
    cv2.destroyAllWindows()

#object detection using a jpg image
def stillImage(model,path):
   
    #Predict what objects are in the image
    result=model(path, conf=0.5) #CONF means that is has to be >50% sure that the object is there
    result=result[0]

    #How Many Objects are detected
    print(len(result.boxes))

    #Go through all objects detected, get name, confidence level, and the coordinates of the object in the image
    for box in result.boxes: #This loop is not needed in final product
        label=result.names[box.cls[0].item()]
        cords=[round(x) for x in box.xyxy[0].tolist()]
        confidence=round(box.conf[0].item(),2)
        print("Object Type: ",label)
        print("Coordinates: ",cords)
        print("Confidence: ",confidence)
        print("-------------------------")
    
    #Open the image
    Image.fromarray(result.plot( )[:,:,::-1]).show()


def video(model,path):
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

            #Escape key will close the window
            if(cv2.waitKey(30)==27):
                break
        else:
            break

    camera.release()
    cv2.destroyAllWindows()


#Call methods and link to YOLO model
def main():
    #Load the YOLO model
    modelPath="YOLO Method/runs/detect/train/weights/last.pt"
    model=YOLO(modelPath)
    
    imagePath1="YOLO Method/Data/images/train/20230915_122551.jpg"
    imagePath2="YOLO Method/Data/images/train/20230915_124542.jpg"
    imagePath3="YOLO Method/Data/images/train/20230915_124629.jpg"

    videoPath="AMRVideo2.mp4"

    #stillImage(model,imagePath3)
    #liveCamera(model)
    video(model, videoPath)
    

if __name__ == "__main__":
    main()
