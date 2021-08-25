# Here we going to learn how to join the images when we have lots of image

import cv2

import numpy as np

img = cv2.imread("/Users/abhishekraj/Downloads/xa.jpeg")


# hstack is used to add the image in horizontally
imgHor = np.hstack((img,img))

imgVer = np.vstack((img ,img))

cv2.imshow(" Horizontal",imgHor)

cv2.imshow("Vertical",imgVer)

cv2.waitKey(0)