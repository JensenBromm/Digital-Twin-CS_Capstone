#Using YoloV8
import sys
from ultralytics import YOLO
import cv2


#Define Global variables
#Load the YOLO model
modelPath="runs/detect/train3/weights/best.pt"
model=YOLO(modelPath)
#Anything Below Threshold will not be marked
threshold=0.6

#Coordinates of the new origin marker in top down view (Offset)
newOrigin=[124,42]

#Equation to Transalte pixel coordinates to unreal
# Unreal Coordinate X= ScaleX * ImageCoordX - Offset 

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

    # detect objects
    # track objects
    results = model.track(frame, persist=True)[0]

    # plot results
    frame_ = results.plot()

    cords=results.boxes.xyxy.tolist()

    midPoints=[]
    for i in range(len(cords)):
        print("----Unreal Coordinates----")
        #Seperate the coordinates
        x1=cords[i][0]
        y1=cords[i][1]
        x2=cords[i][2]
        y2=cords[i][3]
        
        #Calculate the midpoints of the bounding boxes and translate them to Unreal Coordinates
        midX=scaleX*(((x1+x2)/2) - newOrigin[0])
        midY=scaleY*(((y1+y2)/2) - newOrigin[1])
        print(str(midX)+","+str(midY))
        midPoints.append([midX,midY])
        print("----------------------")

  
    cv2.imshow('frame', frame_)
    #Escape key will close the window
    while True:
        if(cv2.waitKey(30)==27):
            break
    
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

    ret = True
    # read frames
    while ret:
        ret, frame = camera.read()
        if ret:
            # detect objects
            # track objects
            results = model.track(frame, persist=True)[0]

            # plot results
            frame_ = results.plot()

            cords=results.boxes.xyxy.tolist()

            midPoints=[]
            for i in range(len(cords)):
                print("----Unreal Coordinates----")
                #Seperate the coordinates
                x1=cords[i][0]
                y1=cords[i][1]
                x2=cords[i][2]
                y2=cords[i][3]
        
                #Calculate the midpoints of the bounding boxes and translate them to Unreal Coordinates
                midX=scaleX*(((x1+x2)/2) - newOrigin[0])
                midY=scaleY*(((y1+y2)/2) - newOrigin[1])
                print(str(midX)+","+str(midY))
                midPoints.append([midX,midY])
                print("----------------------")

            # visualize
            cv2.imshow('frame', frame_)
            #Escape key will close the window
            if(cv2.waitKey(30)==27):
                break
        else: #Once Frame is done
            camera.release()
            cv2.destroyAllWindows()

def main():
    
    imagePath1="Data/images/train/20230915_122551.jpg" #Upclose Robot
    imagePath2="Data/images/train/Stream1 - frame at 0m1s.jpg" #Starting Lineup Stream1
    imagePath3="Data/images/train/Stream1 - frame at 8m0s.jpg" #Robots with Shelves
    imagePath4="Data/images/train/TopDown - frame at 0m0s.jpg" 
    imagePath5="Data/images/train/TopDown - frame at 1m7s.jpg" 
    videoPath1="Videos/stream1.mp4"
    videoPath2="Videos/speedVideo.mp4"
    videoPath3="Videos/speedVideo2.mp4"
    videoPath4="Videos/TopDown.avi"

    #Can only connect to security camera while on GSU campus
    cameraIP="rtsp://141.165.40.33/stream1"

    #stillImage(imagePath4)
    video(videoPath4)  #This should be able to take in IP as well
    #video(cameraIP)

    

if __name__ == "__main__":
    main()
