#Using YoloV8
import sys
from ultralytics import YOLO
import cv2
from MongoInstance import getDatabase
from TopDownView import createTopDown


#Get the database
dbname = getDatabase()

#SetUp dictonary to communicate with the database
collection_name = dbname["robots"]
robotDict = {
    "_id" :  1,
    "class": "", # This is going to be either "AMR Robot" or "AMR Robot With Shelf"
    "x" : 0,
    "y" : 0
}


#Define Global variables
#Load the YOLO model
modelPath="runs/detect/train3/weights/best.pt"
model=YOLO(modelPath)
names=model.names
#Anything Below Threshold will not be marked
threshold=0.6

#Coordinates of the new origin marker in top down view (Offset) We are using the red marker in the top left of the top down view as the new origin
newOrigin=[124,42]

#Set the Scales between pixel and Unreal
'''
Scales were calculated by setting unreal coordinates and comparing them to the pixel coordinates

Unreal CoordinateX = ScaleX * PixelCoordX - Offset
Unreal CoordinateY= ScaleY* Pixel CoordY - Offset

Using the unreal coordinate and the pixel coordinate you can calculate a scale.
I did this for each robot then found an average of the scales to get a final value for ScaleX and ScaleY
'''
scaleX=0.23
scaleY=0.25

#object detection using a jpg image
def stillImage(path):

    frame=cv2.imread(path)

    # track objects
    results = model.track(frame, persist=True)[0]

    # plot results
    frame_ = results.plot()            
    
    if len(results) > 0:
        #Get needed info from detections
        cords=results.boxes.xyxy.tolist()
        classIDs=results.boxes.cls.tolist()
        trackIDs=results.boxes.id.tolist()

        for i in range(len(cords)):
            #Seperate the coordinates
            x1=cords[i][0]
            y1=cords[i][1]
            x2=cords[i][2]
            y2=cords[i][3]
        
            #Calculate the midpoints of the bounding boxes and translate them to Unreal Coordinates
            unrealX=scaleX*(((x1+x2)/2) - newOrigin[0])
            unrealY=scaleY*(((y1+y2)/2) - newOrigin[1])

            #Get the variables for the database
            name=names[classIDs[i]]
            #Detector will label the robots 1,2,3, or 4
            id=trackIDs[i]
        
            #Robots are identified based off their unique label
            keyValue = {"_id" : id}
            #Update the x and z coordinate. Also, make sure that the class name hasnt changed
            #The database is marked incorrectly the Y axis is marked as the Z axis
            update= {"$set": {"x":unrealX, "z":unrealY, "class":name}} #If the class name changes from robot -> robot with shelf the unreal engine needs to create a new object at that location
            collection_name.update_one(keyValue, update, upsert=True)
    else:
        print("No objects detected")

  
    cv2.imshow('frame', frame_)
    #Escape key will close the window
    """ 
    while True:
        if(cv2.waitKey(30)==27):
            break 
    """

    return results
    
#Object Detection via Pre-Recorded Video or Live Camera Stream (RTSP STREAM)
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

    ret = True
    # read frames
    while ret:
        ret, frame = camera.read()
        if ret:
            #Check if the video is from a live camera feed
            if 'rtsp' in path:
                #If a live camera feed is being used, a top down view needs to be constructed
                frame=createTopDown(frame)

            # track objects
            results = model.track(frame, persist=True)[0]

            # plot results
            frame_ = results.plot()

            if len(results) > 0:
                #Get needed info from detections
                cords=results.boxes.xyxy.tolist()
                classIDs=results.boxes.cls.tolist()
                trackIDs=results.boxes.id.tolist()

                for i in range(len(cords)):
                #Seperate the coordinates
                    x1=cords[i][0]
                    y1=cords[i][1]
                    x2=cords[i][2]
                    y2=cords[i][3]
        
                    #Calculate the midpoints of the bounding boxes and translate them to Unreal Coordinates
                    unrealX=scaleX*(((x1+x2)/2) - newOrigin[0])
                    unrealY=scaleY*(((y1+y2)/2) - newOrigin[1])

                    #Get the variables for the database
                    name=names[classIDs[i]]
                    #Detector will label the robots 1,2,3, or 4
                    id=trackIDs[i]
        
                    #Robots are identified based off their unique label
                    keyValue = {"_id" : id}
                    #Update the x and z coordinate. Also, make sure that the class name hasnt changed
                    #The database is marked incorrectly the Y axis is marked as the Z axis
                    update= {"$set": {"x":unrealX, "z":unrealY, "class":name}} #If the class name changes from robot -> robot with shelf the unreal engine needs to create a new object at that location
                    collection_name.update_one(keyValue, update, upsert=True)
            else:
                print("No objects detected")
            # visualize
            cv2.imshow('frame', frame_)
            #Escape key will close the window
            if(cv2.waitKey(30)==27):
                break
        else: #Once Video is done
            camera.release()
            cv2.destroyAllWindows()

    return results

def main():
    
   
    imagePath1="Data/images/train/TopDown - frame at 0m0s.jpg" 
    imagePath2="Data/images/train/TopDown - frame at 1m7s.jpg" 
    
    videoPath="Videos/TopDown.avi"

    #Can only connect to security camera while on GSU campus
    cameraIP="rtsp://141.165.40.33/stream1"

    #Object detection based on a still image
    #stillImage(imagePath1)

    #Object detection based on a video or camera stream
    video(videoPath)
    #video(cameraIP)

    

if __name__ == "__main__":
    main()
