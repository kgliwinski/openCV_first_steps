import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

PATH = 'Resources/Photos/'

img = cv.imread(PATH + 'cats.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Thresholding is a binarization of an image ->
# if below threshhold the pixel is set to 0, otherwise it is set to 255

# 1. Simple thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Simple thresholded', thresh)

# 2. Invershe thresholding

threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple thresholded inverted', thresh_inv)

# 3. Adaptive thresholding -> letting the cv find the optimal thresholding val
# C value is a integer substracted from the mean, used to fine-tuning thresholding
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, blockSize=11, C=3)

cv.imshow('Adaptive thresholding', adaptive_thresh)


cv.waitKey(0)
