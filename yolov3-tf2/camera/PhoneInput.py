import urllib
import cv2
import numpy as np
import ssl

cap = cv2.VideoCapture(0)
address = "http://10.0.0.234:8080/video" 

cap.open(address)

if (cap.isOpened()== False): 
    print("Error opening video stream or file")

# Read and display video frames until video is completed or 
# user quits by pressing ESC
cv2.startWindowThread()
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Display the resulting frame
        cv2.imshow('Frame',frame)
        if (cv2.waitKey(1) & 0xFF == 27):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()