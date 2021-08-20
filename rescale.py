import cv2 as cv

img  = cv.imread('Photos/dog_small.jpg')
cv.imshow('dog', img)

def rescaleFrame(frame, scale=0.75):
    # Images, Video, and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

def changeRes(width, height):
    # Live Video
    capture.set(3, width)
    capture.set(4, height)


# Reading Videos
capture = cv.VideoCapture('Videos/Spider.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

