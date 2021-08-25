# Here we are going to learn the shape and size
import cv2
import numpy as np

# First we are going to create a matrix which is filled with 0s used numpy library of python.0 means black
imgBlack =np.zeros((512,512,3),np.uint8)  # it is a greyscale image

# imgBlack[:]=255,0,0
# Check the dimentionality of image
# print(imgBlack.shape)
imgWhite = np.ones((512,512))

# Draw the line
cv2.line(imgBlack,(0,0),(300,300),(0,255,0),3)
# Draw the rectangle
cv2.rectangle(imgBlack,(0,0),(250,350),(0,0,250),3)
# Draw the Circle
cv2.circle(imgBlack,(250,350),30,(255,255,0),3)

# write Some Text
cv2.putText(imgBlack,"Abhishek",(300,200),cv2.FONT_HERSHEY_DUPLEX,1,(0,160,0),2)

# IF u want to fill the rectangle we have to use cv2.FILLED


cv2.imshow("Black",imgBlack)
cv2.imshow("White",imgWhite)


cv2.waitKey(0)
