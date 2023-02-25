import cv2 as cv
import numpy as np

PATH = 'Resources/Photos/'

img = cv.imread(PATH + 'group 1.jpg')
cv.imshow('Group', img)

# 1. Translation

def translate(img, x, y):
    # creating translation matrix
    transMat = np.float32([[1,0,x], [0,1,y]])
    # width, height
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)

# -x -> left
# -y -> Up
# +x -> right
# +y -> Down

# translation right by 100 px, and down by 100px
translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

translated_2 = translate(img, -100, 100)
cv.imshow('Translated 2', translated_2)

# 2. Rotation (by some angle)

# specify any point to rotate about (rotpoint), angle>0 is counterclockwise
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 30)
cv.imshow('Rotated', rotated)

# rotating once created the black triangles, which will be always present
rotated_twice = rotate(rotated, -30)
cv.imshow('Back to normal (but cropped)', rotated_twice)

# 3. Resizing the image

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# 4. Flipping an image

# flipCode can be eiher 0 (vartical flip), 1 (flip horizontaly), -1 (both vertically and horizontally)
flip_ver = cv.flip(img, flipCode=0)
cv.imshow('Flipped vertically', flip_ver)

flip_hor = cv.flip(img, flipCode=1)
cv.imshow('Flipped horizontally', flip_hor)

flip_both = cv.flip(img, flipCode=-1)
cv.imshow('Flipped both ways', flip_both)

# 5. Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)