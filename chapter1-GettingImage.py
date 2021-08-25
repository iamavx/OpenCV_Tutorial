# Here we are going to read the image
import cv2
import numpy as np




# for reading image we have a method called "imread"

img = cv2.imread("/Users/abhishekraj/Downloads/xa.jpeg")
imgGray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,100,100)


# taking the matrix size of 5 as a kernel

kernel = np.ones((5,5),np.uint8)
imgDilation = cv2.dilate(img ,kernel ,iterations=1) # iteration is something that how much you dilate or erode the image
imgErode = cv2.erode(img ,kernel ,iterations=1)

# Dilation and erosion are the two morphological operation that process the image based on their shape .
cv2.imshow("output", img)


# To convert gray imag we have to use a method "cvtColor" which contain different colour spaces.there is a kernel
# which are the matrix of odd size(3,5,7).Dilation is used to increase the object area i.e it will increase the white
# area in the image

cv2.imshow("GrayImage",imgGray)

# Convert image into blur image we use the method called "GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Blur",imgBlur)
cv2.imshow("CannyImage",imgCanny)
cv2.imshow("Dilation",imgDilation)
cv2.imshow("Erosion",imgErode)
cv2.waitKey(0)