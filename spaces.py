import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/tokyo.jpg')
cv.imshow('Tokyo', img)

# plt.imshow(img)
# plt.show()

# BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

# BGR TO HLS
hls = cv.cvtColor(img, cv.COLOR_BGR2HLS)
cv.imshow("hls", hls)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb", rgb)

# HSV to BGR 
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("lab --> BGR", lab_bgr)

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)