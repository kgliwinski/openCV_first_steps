import cv2 as cv

PATH = '../Resources/Photos/'
img = cv.imread(PATH + 'cat.jpg')
cv.imshow('Cat', img)

# 1. Converting to gray scale