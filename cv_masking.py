import cv2 as cv
import numpy as np

PATH = 'Resources/Photos/'

img = cv.imread(PATH + 'cats.jpg')
cv.imshow('Cat', img)

# Dimensions of the mask must be the same as the image
blank = np.zeros(img.shape[:2], dtype='uint8')

# 1. Basic mask
basic_mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2 ), 100, 255, -1)
cv.imshow('Mask', basic_mask)

# Essentialy a circle in the center
masked = cv.bitwise_and(img, img, mask=basic_mask)
cv.imshow('Masked image', masked)

cv.waitKey(0)