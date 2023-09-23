from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  
import numpy as np
import cv2
import time

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("Python Scripts/keras_Model.h5", compile=False)

# Load the labels
class_names = open("Python Scripts/labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

#open camera
camera=cv2.VideoCapture(0)

#get the time to only print results every couple of seconds
lasttime=time.time()
#Run Object detection
while True:
    # Grab the webcamera's image.
    ret, image = camera.read()
    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    # Make all values in image on a scale from 0-1
    image = (image / 127.5) - 1

    
    # Predicts the model
    prediction = model.predict(image) #opens the model and determines what image is being shown
    index = np.argmax(prediction) #gets the index of the object with the highest confidence score
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    if(time.time()-lasttime >=2):
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
        lasttime=time.time()
    

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

camera.release()
cv2.destroyAllWindows()
