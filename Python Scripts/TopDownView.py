import cv2
import numpy as np

#Create the top down view frame by frame
def createTopDown(frame):

    #Resize frame to fit hardcoded pixel coordinates
    frame=cv2.resize(frame, (1280,720))
    # Define the desired width and height of the transformed video
    new_width = 900
    new_height = 1000

    # Define the coordinates of the four points (These points are hard coded for frames that are 720p)
    points = [(766 , 630), (999 , 155), (422 , 10), (158 , 230)]

    new_points = np.array([[0, 0], [new_width, 0], [new_width, new_height], [0, new_height]], dtype=np.float32)

    #Warp frame to create the top down view
    matrix = cv2.getPerspectiveTransform(np.array(points, dtype=np.float32), new_points)
    frame = cv2.warpPerspective(frame, matrix, (new_width, new_height))

    return frame

def getPoints(path):
    # Load the video
    cap = cv2.VideoCapture(path)

    if not cap.isOpened():
        print("Error: Unable to load the video.")
        exit(1)
    # Define the coordinates of the four points
    points = []

    def on_mouse(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if len(points) < 4:
                points.append((x, y))
                print("Point "+str(len(points))+": ("+str(x)+" , "+str(y)+")")
                cv2.circle(frame_with_dots, (x, y), 5, (0, 0, 255), -1)
                cv2.imshow('Video', frame_with_dots)

    cv2.namedWindow('Video')
    cv2.setMouseCallback('Video', on_mouse)

    while len(points) < 4:
        ret, frame = cap.read()
        if not ret:
            break
        frame_with_dots = frame.copy()  # Create a copy of the frame to draw dots on
        cv2.imshow('Video', frame_with_dots)
        key = cv2.waitKey(0)  # Wait indefinitely until a key is pressed
        if key == 27:  # Press Esc to exit
            break

    cap.release()
    cv2.destroyAllWindows() 

    return points