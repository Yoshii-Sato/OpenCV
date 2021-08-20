import cv2 as cv

img = cv.imread('Photos/dog_small.jpg')
cv.imshow('Dog', img)

# averaging
average = cv.blur(img, (3,3))
cv.imshow("average blur", average)

# gaussian blur - less blurring - but more natural compared to averagign
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("gaussian blur", gauss)

# median blur - better at reducing the amount of noise
median = cv.medianBlur(img, 3)
cv.imshow("median blur", median)

# bilateral blurring
bilateral = cv.bilateralFilter(img, 50, 15, 15)
cv.imshow("bilateral", bilateral)

cv.waitKey(0)