import cv2 as cv

# Reading videos

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    # if letter d is pressed, it will break
    if cv.waitKey(20) & 0xFF==ord('d'): 
        break

capture.release()

# assertion failed -215: it means that the video ran out of frames
# OR the path is wrong (in case of images and videos)

cv.destroyAllWindows()