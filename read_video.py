import cv2 as cv

# rescaling frames - works on both videos(frames) and images
def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)  # frame[1] - width
    height = int(frame.shape[0] * scale)  # frame[0] - height
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Reading and showing videos
def video_capture(source, scale=0.75):
    capture = cv.VideoCapture(source)

    while True:
        isTrue, frame = capture.read()
        
        new_frame = rescale_frame(frame)
        
        cv.imshow('Video', frame)
        cv.imshow('Video_rescaled', new_frame)

        # if letter d is pressed, it will break
        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    capture.release()

    # assertion failed -215: it means that the video ran out of frames
    # OR the path is wrong (in case of images and videos)

    cv.destroyAllWindows()

# changing the resolution of live video
def change_res(capture, width, height):
    capture.set(3, width)
    capture.set(4, height)

video_capture(0)
