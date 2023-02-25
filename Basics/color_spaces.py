import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

PATH = 'Resources/Photos/'

img = cv.imread(PATH + 'park.jpg')
cv.imshow('Park', img)

# 1. BGR to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. BGR to HSV (hue saturation value)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# 3. BGR to LAB (l*a*b)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab', lab)

# 4. Displaying img (it is BGR) - inversion of colors
# plt.imshow(img)
# plt.show()

# 5. BGR to RGB - inverted colors
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# Grayscale to HSV directly won't work

# 6. HSV to BGR

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV_BGR', hsv_bgr)

# 7. LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB_BGR', lab_bgr)

cv.waitKey(0)