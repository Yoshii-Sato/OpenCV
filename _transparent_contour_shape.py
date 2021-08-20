import cv2 as cv
import numpy as np
import random

image = cv.imread('Photos/dog_small.jpg')
  
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray, 200, 210)

# cv.imshow('canny', canny)

copy = canny.copy()
contours, hierarchy = cv.findContours(copy, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

# print(contours)
# print(hierarchy)



def add_random_boxes(img_link, amount):
    temp_img = cv.imread(img_link)

    # shapes = np.zeros_like(img, np.uint8)
    blank = np.zeros(temp_img.shape, dtype='uint8')

    for repetition in range(amount):
        x = random.randint(0, temp_img.shape[1]-100)
        y = random.randint(0, temp_img.shape[0]-100)
        cv.rectangle(blank, (x,y), (x+100, y+100), (255,255,255), -1)
    
    alpha = .5
    mask = blank.astype(bool)
    temp_img[mask] = cv.addWeighted(temp_img, alpha, blank, 1 - alpha, 0)[mask]
    
    cv.imshow('blank', blank)
    cv.imshow('return', temp_img)

def add_boxes(img, coords):
    blank = np.zeros((1000,1000,3), dtype = 'uint8')
    blank.fill(255)

    for coord in coords:
        cv.rectangle(blank, coord[0], coord[1], (255,0,0), -1)
    
    cv.imshow('blank', blank)

def checker_board(l, w, number):
    pass

def create_contours(h,w,points):
    # change into a numpy array - you cant change the data type
    points = np.array([points])

    img = cv.imread('Photos/tokyo.jpg')
    blank = np.zeros(img.shape, dtype = 'uint8')
    blank_copy = blank.copy()

    copy = img.copy()
    cv.drawContours(blank, points, -1, (255,1,1), thickness = -1)

    alpha = .5
    mask = blank.astype(bool)
    copy[mask] = cv.addWeighted(img, alpha, blank, 1 - alpha, 0)[mask]

    cv.imshow('tokyo', copy)
    cv.imshow('blank', blank)

def create_random_contour(x, y, number_of_points):

    blank = np.zeros((x,y,3), dtype= 'uint8')
    blank.fill(255)

    points = []

    for i in range(number_of_points):
        x_coord = random.randint(1,500)
        y_coord = random.randint(1,500)
        points.append([x_coord,y_coord])
        
    points = np.array([points])    
    cv.drawContours(blank, points, -1, (255,0,0), -1)

    cv.imshow('random contours', blank)


# cv.imshow('aot', black)
# cv.imwrite('aot_changed.jpg', img)

# add_random_boxes('Photos/endgame.jpg', 10)

# img = cv.imread('Photos/dog_small.jpg')
# add_boxes(img, coords = [[(100,100), (200,200)], [(300,300), (400,400)], [(500,500), (600,600)]])

points = [[200,100],[300,300],[500,400],[100,300],[100,100]]
create_contours(500,500,points)

# create_random_contour(500,500,500)

cv.waitKey(0)