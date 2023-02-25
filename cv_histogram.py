import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

PATH = 'Resources/Photos/'

img = cv.imread(PATH + 'cats.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Dimensions of the mask must be the same as the image
blank = np.zeros(img.shape[:2], dtype='uint8')


# 1. Histogram of the gray image

# channels -> [0] (as it is gray)
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 255])

plt.figure(1)
plt.title('Grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('Num. of pixels')
plt.plot(gray_hist)
plt.xlim([0, 255])

# 2. Setting a mask for the histogram (picking an area of the image to histogram)
circle = cv.circle(blank, (img.shape[1] // 2, img.shape[1] // 2), 100, 255, -1)

mask = cv.bitwise_and(gray, gray, mask = circle)

gray_hist_masked = cv.calcHist([gray], [0], mask, [256], [0, 255])

plt.figure(2)
plt.title('Grayscale histogram with mask')
plt.xlabel('Bins')
plt.ylabel('Num. of pixels')
plt.plot(gray_hist_masked)
plt.xlim([0, 255])
# plt.show()

# 3. Color histogram

img_mask = cv.bitwise_and(img, img, mask=circle)
colors = ('b', 'g', 'r')
    
plt.figure(3)
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,255])
    plt.plot(hist, color=col)
    plt.title('Grayscale histogram with mask')
    plt.xlabel('Bins')
    plt.ylabel('Num. of pixels')
    plt.xlim([0, 255])

plt.show()

cv.waitKey(0)
