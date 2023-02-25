import cv2 as cv
import numpy as np

PATH = 'Faces/val/elton_john/'

# Face detection -> detects if the face is present in the image
# Classifier: algorithm that decides whether image is positive (face is present) or negative
# We will be using the haar cascade - the basic one, more prone to errors due to some noise

# Using the haarcascade_frontalface_default.xml from opencv xml, 
# which is stored in the haar_face.xml file

elton = cv.imread(PATH + '1.jpg')
cv.imshow('Elton', elton)

gray = cv.cvtColor(elton, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Elton', gray)

# Face detection does not involve skin color or other
# It just looks at edges and tries to determine whether its a face

# 1. Reading the xml file
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# faces_rect is essentialy a coordinate of the faces found in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
print(len(faces_rect))

# We can draw a rectangle over the detected faces
for(x,y,w,h) in faces_rect:
    cv.rectangle(elton, (x,y), (x+w, y+h), (0,255,0), 2)

cv.imshow("Detected face", elton)

img2 = cv.imread('../Basics/Resources/Photos/group 1.jpg')
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

faces_rect_img = haar_cascade.detectMultiScale(gray2, scaleFactor=1.1, minNeighbors=3)
print(len(faces_rect_img))

for(x,y,w,h) in faces_rect_img:
    cv.rectangle(img2, (x,y), (x+w, y+h), (0,255,0), 2)

# DOES NOT SHOW ALL - SUSCEPTIBLE TO NOISE
cv.imshow('Group faces', img2)

# To minimize bad behaviour like above, you should play around with scaleFactor and minNeighbors

img3 = cv.imread('../Basics/Resources/Photos/group 1.jpg')
gray3 = cv.cvtColor(img3, cv.COLOR_BGR2GRAY)

faces_rect_img2 = haar_cascade.detectMultiScale(gray3, scaleFactor=1.1, minNeighbors=1)
print(len(faces_rect_img2))

for(x,y,w,h) in faces_rect_img2:
    cv.rectangle(img3, (x,y), (x+w, y+h), (0,255,0), 2)

# Still not perfect - minimising values still made it better - the algorithm got MORE susceptible to noise tho
cv.imshow('Better group faces', img3)

cv.waitKey(0)