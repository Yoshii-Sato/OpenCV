import cv2 as cv

img  = cv.imread('Photos/dog_small.jpg')

cv.imshow('dog', img)

cv.waitKey(0)

# capture = cv.VideoCapture('Videos/Spider.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

