# Have you ever thought about the possibility of using your phone’s camera for computer vision task? Yes, you can!

# Learn How To Use Phone Camera with Python:
# Using a phone camera with Python is very useful for those who are planning to create computer vision apps that will use a smartphone camera as a part of your application. Here I am using Python on Windows 10. Hope this works for other operating systems as well, but if you are using Windows then don’t worry just follow the steps mentioned below.

# The process of using a phone camera with Python:

# First, install the OpenCV library in Python; pip install opencv-python.
# Download and install the IP Webcam application on your smartphones.
# After installing the IP Webcam app, make sure your phone and PC are connected to the same network. Run the app on your phone and click Start Server.
# After that, your camera will open with an IP address at the bottom. Copy the IP address as we will need to use it in our Python code to open your phone’s camera.
# Now let’s code to see how to open a phone camera with Python for the tasks of computer vision:

# Code :

import cv2
import numpy as np

url = "https://192.168.1.47:8080/video"
cap = cv2.VideoCapture(url)

while True:
    ret, frame = cap.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break
cv2.destroyAllWindows()

# In a few moments, an OpenCV window will appear and do the rest. To close the window, just press any key. This is how to connect a phone’s camera with Python for computer vision applications. The next step on how to use this feature depends on how you want to use it.