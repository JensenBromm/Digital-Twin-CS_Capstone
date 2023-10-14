import cv2
import numpy as np

# Load the image
image = cv2.imread('Data/images/train/Stream1 - frame at 0m1s.jpg')

if image is None:
    print("Error: Unable to load the image.")
else:
    # Define the coordinates of the four points
    points = []

    def on_mouse(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if len(points) < 4:
                points.append((x, y))
                cv2.circle(image, (x, y), 5, (0, 0, 255), -1)
                cv2.imshow('Image', image)

    cv2.imshow('Image', image)
    cv2.setMouseCallback('Image', on_mouse)

    while len(points) < 4:
        cv2.waitKey(1)

    cv2.destroyAllWindows()

    # Define the desired width and height of the transformed image
    new_width = 700
    new_height = 1000

    new_points = np.array([[0, 0], [new_width, 0], [new_width, new_height], [0, new_height]], dtype=np.float32)

    matrix = cv2.getPerspectiveTransform(np.array(points, dtype=np.float32), new_points)

    # Perform a perspective transformation
    result_perspective = cv2.warpPerspective(image, matrix, (new_width, new_height))

    # Display the perspective-transformed image
    cv2.imshow('Top-Down View (Perspective)', result_perspective)

    # Save the final image
    cv2.imwrite('output_image.jpg', result_perspective)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
