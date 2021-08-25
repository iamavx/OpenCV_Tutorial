import cv2
import numpy as np

# Scaling operation increases/reduces size of an image.

img = cv2.imread("/Users/abhishekraj/Downloads/xa.jpeg")

# Get number of pixel horizontally and vertically.
(height, width) = img.shape[:2]

# Specify the size of image along with interploation methods.
# cv2.INTER_AREA is used for shrinking
# whereas cv2.INTER_CUBICis used for zooming.
res1 = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_AREA)

# Rotation of Image

M = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)
res2= cv2.warpAffine(img, M, (width, height))

# Edge Detection

# Canny edge detection.
edges = cv2.Canny(img, 100, 200)

cv2.imshow("Scaling Image",res1)
cv2.imshow("Rotation",res2)
cv2.imshow("Canny",edges)



cv2.waitKey(0)
