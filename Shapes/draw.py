import cv2 as cv
import numpy as np

PATH = '../Resources/'

# the 3 is the number of colors
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Painting an image with a color
blank[:] = 0, 0, 255  # [:] is referencing the whole image
cv.imshow('Red', blank)

blank[:] = 0, 255, 0  # [:] is referencing the whole image
cv.imshow('Green', blank)

# giving a range of pixels
blank[200:300, 300:400] = 0, 0, 254
cv.imshow('Part', blank)

# 2. Draw a rectangle
blank2 = np.zeros((500, 500, 3), dtype='uint8')
# object, origin, end, color, thickness
# cv.rectangle(blank2, (0,0), (250,500), (0,255,0), thickness=2)
# cv.imshow('Rectangle', blank2)
# could also use the blank[1].shape (widht), blank[0].shape height and divide
cv.rectangle(blank2, (0, 0),
             (blank2.shape[1]//2, blank2.shape[0]), (0, 255, 0), thickness=2)
cv.imshow('Rectangle', blank2)

# full rectangle
blank3 = np.zeros((500, 500, 3), dtype='uint8')
cv.rectangle(blank3, (0, 0), (250, 500), (0, 255, 0), thickness=-1)
cv.imshow('Rectangle_full', blank3)

# 3. Circle
# blank4 = np.zeros((500, 500, 3), dtype='uint8')
# object, center, radius, color, thickness
cv.circle(blank3, (blank3.shape[1] // 2,
          blank3.shape[0]//2), 40, (0, 0, 255), thickness=3)
cv.imshow('Circle', blank3)

# 4. draw a line
# same as rectangle, but with .line
cv.line(blank2, (0, 0),
             (blank2.shape[1]//2, blank2.shape[0]), (255, 0, 0), thickness=2)
cv.imshow('Line', blank2)

# 5. Text
# object, text, position, font, fontscale, color, thickness
cv.putText(blank2, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,123,255), 2)
cv.imshow('Hello', blank2)

cv.waitKey(0)

cv.destroyAllWindows()
