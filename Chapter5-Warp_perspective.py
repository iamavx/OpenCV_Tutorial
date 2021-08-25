# OpenCV provides a function cv2. getPerspectiveTransform() that takes as input the 4 pairs of corresponding points
# and outputs the transformation matrix . warpPerspective() function that applies the perspective transformation to
# an image.

import cv2
import numpy as np

img = cv2.imread("/Users/abhishekraj/Downloads/xa.jpeg")
cv2.imshow("Output",img)
cv2.waitKey(0)
