# Here we are going to learn how to import a video in opencv
import cv2

# To import video we have a method "videoCaptured"

cap = cv2.VideoCapture("/Users/abhishekraj/Downloads/video.mp4")

# cap = cv2.VideoCapture(1)

# cap.set(3,640)

# cap.set(4,480)

# To set the brightness of video
# cap.set(10,100)

# video is a collection of image so , we have needed a loop to see each frame one by one

while True:
    # read method save or read  the image in img and i will indicates that either it is saved successfully or not
    success, img = cap.read()
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
