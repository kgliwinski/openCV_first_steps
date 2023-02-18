import cv2 as cv
PATH = '../Resources/Photos/'

img = cv.imread(PATH + 'cat.jpg')

cv.imshow('Cat', img)

cv.waitKey(0) # waits infinitely for keyboard to be pressed 

cv.destroyAllWindows()