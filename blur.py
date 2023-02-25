import cv2 as cv
import numpy as np


PATH = 'Resources/Photos/'

img = cv.imread(PATH + 'cats.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# When applying blur - what happens?

# 1. Averaging - average the pixel intensity as the average of the surrounding pixels intensity

average = cv.blur(img, (3,3))
cv.imshow('Average', average)

# Bigger mask -> more blur

average_more = cv.blur(img, (3,3))
cv.imshow('More average', average_more)

# 2. Gaussian blur - instead of the average, we have weights on the pixels in proximity
# Overall less blur

gauss = cv.GaussianBlur(img, (3,3), sigmaX=0)
cv.imshow('Gaussian blur', gauss)

# 3. Median blur - Same thing as averaging, but taking median instead of averaging
# Not a (3,3) bit just 3 as kernel size
median = cv.medianBlur(img, 3)
cv.imshow('Median blur', median)

# 4. Bilateral bluring - the most effective, it does blur but retains the edges of the image
# The edges are still there
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral blur', bilateral)


cv.waitKey(0)