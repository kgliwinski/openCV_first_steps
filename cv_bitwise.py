import cv2 as cv
import numpy as np


PATH = 'Resources/Photos/'

img = cv.imread(PATH + 'cats.jpg')
cv.imshow('Cat', img)

blank = np.zeros((400,400), dtype='uint8')

# Basic bitwise operations: and, or, not, xor

rectangle = cv.rectangle(blank.copy(), (30, 30), (370,370), color=255, thickness=-1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# 1. Bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise and', bitwise_and)

# 2. Bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise or', bitwise_or)

# 3. Bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise xor', bitwise_xor)

# 4. Bitwise NOT
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT', bitwise_not)

cv.waitKey(0)