import cv2

image = cv2.imread("/Users/abhishekraj/Downloads/xa.jpeg")

# Window name in which image is displayed
window_name = 'Image'

# Using cv2.copyMakeBorder() method
image = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value=0)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)