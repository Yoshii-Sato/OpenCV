import cv2 as cv
import numpy as np

img = cv.imread('Photos/aot.jpg')
cv.imshow('aot', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# blur = cv.GaussianBlur(gray, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("Blurred", blur)

canny = cv.Canny(img, 50, 60)
cv.imshow("Canny", canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow("Thresh", thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv. CHAIN_APPROX_NONE)
print(f'{len(contours)} contours(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)


cv.waitKey(0)