import cv2 as cv
import numpy as np


PATH = 'Resources/Photos/'

img = cv.imread(PATH + 'park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# 1. Splitting an image into three color chanels

b,g,r = cv.split(img)

# These will be shown as grayscale
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape, b.shape, g.shape, r.shape)

# 2. Merging the color channels
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

# 3. Showing the actual color in the split by color images

blue = cv.merge([b,blank,blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue_b', blue)
cv.imshow('Green_b', green)
cv.imshow('Red_b', red)

cv.waitKey(0)