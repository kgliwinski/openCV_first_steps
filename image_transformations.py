import cv2 as cv

PATH = 'Resources/Photos'

img = cv.imread(PATH + 'group 1.jpg')
cv.imshow('Group', img)

# 1. Translation


cv.waitKey(0)