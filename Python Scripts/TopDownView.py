import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture('Videos/speedVideo.mp4')

if not cap.isOpened():
    print("Error: Unable to load the video.")
    exit(1)

# Define the desired width and height of the transformed video
new_width = 900
new_height = 1000

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

new_points = np.array([[0, 0], [new_width, 0], [new_width, new_height], [0, new_height]], dtype=np.float32)

# Define the codec and create a VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # You can change the codec as needed
out = cv2.VideoWriter('filename.avi',  cv2.VideoWriter_fourcc(*'MJPG'), 10, (new_width,new_height))  # Adjust frame rate as needed

while True:
    ret, frame = cap.read()
    if not ret:
        break

    matrix = cv2.getPerspectiveTransform(np.array(points, dtype=np.float32), new_points)
    result_perspective = cv2.warpPerspective(frame, matrix, (new_width, new_height))

    cv2.imshow('Top-Down View (Perspective)', result_perspective)
    out.write(result_perspective)  # Write the frame to the output video

    key = cv2.waitKey(1)
    if key == 27:  # Press Esc to exit
        break

cap.release()
#out.release()  # Release the output video
cv2.destroyAllWindows()
