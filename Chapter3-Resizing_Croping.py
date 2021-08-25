# Hey Dear , the convention of plotting the graph is different from mathematical representation
# x-axis is same as x-axis and y-axis is opposite to y-axis
import cv2

img = cv2.imread("/Users/abhishekraj/Downloads/xa.jpeg")

# Image is just the array of pixel or matrix

print(img.shape)

# Resize the image
imgResize = cv2.resize(img, (300, 200))

# Cropping an image ,No requirement of cv2 here
# Note in cropping height comes first then width comes

imgCropped =img[0:200,200:500] # img[height,width]
cv2.imshow("Output", img)
cv2.imshow("Resize", imgResize)
cv2.imshow("Cropped", imgCropped)

cv2.waitKey(0)
