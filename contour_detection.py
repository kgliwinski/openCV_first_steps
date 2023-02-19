import cv2 as cv
import numpy as np

PATH = 'Resources/Photos/'

img = cv.imread(PATH + 'cats 2.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 100, 150)
cv.imshow('Canny Edges', canny)

# 1. Finding countours

def find_contours(img):
    contours, hierarchies = cv.findContours(
        img, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    contours2, hierarchies2 = cv.findContours(
        img, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    print(f'{len(contours)} contours found in none approx, {len(contours2)} contours found in simple approx')

    # cv.drawContours(blank, contours, -1, (0,0,255), 2)
    # cv.imshow('Contours drawn', blank)
    return contours

# 2nd arg -> sets mode in which it returns contours
# RETR_TREE -> all hierarchichal contours
# RETR_EXTERNAL -> only external contours
# RETR_LIST -> all the contours in image

# 3rd arg -> approximation methods
# NONE -> all contours (i.e. if its a line, it will give all coordinates of points)
# SIMPLE -> compresses all the contours (i.e. if line, it will only give endpoints)

# contours -> python list of all the contours in the image
# hierarchies -> hierarchical representation of contours

cont_1 = find_contours(canny)

# draw contours draws the 
cv.drawContours(blank, cont_1, -1, (0,0,255), 1)
cv.imshow('Contours drawn 1', blank)

blank = np.zeros(img.shape, dtype='uint8')

# 2. Bluring the image before finding edges
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny_blur = cv.Canny(blur, 100, 150)

cont_2 = find_contours(blur)
cv.drawContours(blank, cont_2, -1, (0,0,255), 1)
cv.imshow('Contours drawn 2', blank)

blank = np.zeros(img.shape, dtype='uint8')
# After bluring, the number of contours has deminished by a lot (5 times in)

# 3. Using treshhold first
ret, tresh = cv.threshold(gray, 125, 255, type=cv.THRESH_BINARY)
cv.imshow('Treshhold', tresh)

cont_3 = find_contours(tresh)
cv.drawContours(blank, cont_3, -1, (0,0,255), 1)
cv.imshow('Contours drawn 3', blank)



cv.waitKey(0)
