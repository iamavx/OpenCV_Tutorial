#Face detection using Haar cascades is a machine learning based approach
# where a cascade function is trained with a set of input data.
# OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc.

import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread("/Users/abhishekraj/Downloads/lena.png")

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow("Output", img)
cv2.waitKey(0)
