import cv2 as cv

PATH = 'Resources/Photos/'
img = cv.imread(PATH + 'cat.jpg')
cv.imshow('Cat', img)

# 1. Converting to gray scale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# 2. Blur images
# essentialy removing a noise in the image

# image, kernel size(odd), 
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)

#increased blur - biggest kernel size 
blurred_more = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)

cv.imshow('Blur', blur)
cv.imshow('Blurred more', blurred_more)

# 3. Edge cascade - edge detector
# Canny edge detector

# image, bottom treshhold, top treshhold
canny = cv.Canny(img, 125, 175)

# Lower treshhold
canny_lower = cv.Canny(img, 50, 200)

# By passing a blured image - only some of the contours will be detected
# (the more apparent ones)
canny_blur = cv.Canny(blurred_more, 125, 175)

cv.imshow('Canny', canny)
cv.imshow('Canny lower', canny_lower)
cv.imshow('Canny blur', canny_blur)

# 4. Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)

cv.imshow('Dilated', dilated)
# 5. Eroting the dilated image
eroted = cv.erode(dilated, (7,7), iterations=3)

cv.imshow('Eroted', eroted)

# 6. Resize an image - does what it says, ignores the aspect ratio

# the default is inter area, for resizing for larger dimensions
# you would use cv.INTER_CUBIC. its slower, but better
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA) 

resize_better = cv.resize(img, (2000, 2000), interpolation=cv.INTER_CUBIC)

cv.imshow('Resized', resize)
cv.imshow('Resised to large', resize_better)

# 7. Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)

