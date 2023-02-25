import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

PATH = 'Resources/Photos/'

img = cv.imread(PATH + 'park.jpg')
cv.imshow('Park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Gradients -> edge like regions, present in the image
# Not necesserily the same thing, but gradients can be approximated as edges

# 1. Laplacian

lap = cv.Laplacian(gray, cv.CV_64F)
# The conversion to absolute is necessary for the image to be displayed,
# as the laplacian method will give either positive or negative values when 
# the gradient is from one side or from another
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# 2. Sobel -> gradient in two directions (x and y)
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow('Sobel x', sobelx)
cv.imshow('Sobel y', sobely)

sobelxy = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined sobel', sobelxy)

# 3. Canny edge detector

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)


cv.waitKey(0)
