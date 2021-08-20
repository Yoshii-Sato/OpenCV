import cv2 as cv

img = cv.imread('Photos/dog_small.jpg')
cv.imshow('Dog', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur an image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)
# keep kernel size odd

# Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Images", canny)

# dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations = 1)
cv.imshow("Eroded", eroded)

# resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)

# cropping
cropped = img[50:200, 200:400]
cv.imshow("cropped",cropped)

cv.waitKey(0)