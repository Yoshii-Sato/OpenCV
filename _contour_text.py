import cv2 as cv
import numpy as np

# So we need to build a tool that would do the following:
# Take an input opencv image, contour coordinates (for now just 1 contour at a time), and a string that represents text within that contour
# Draw the contour and fill it with some transparent color
# Draw the text inside the contour in black color, such that the text would fit right in
# For now you can assume that the contour will be always a rectangle. 
# At the beginning you can also assume that the rectangles will not have any rotation. 
# After you cover that base case, you can start thinking about how you would do that for rectangles that have some small rotation (less than 45 degrees)

class Create_Contours_and_Text:
    def __init__(self, text, top_left, h, w) -> None:
        x = top_left[0]
        y = top_left[1]
        self.points = [[x,y], [x+w,y], [x+w, y+h], [x,y+h]]
        self.top_left = top_left
        self.h = h
        self.w = w
        self.text = text
        self.img = cv.imread('Photos/tokyo.jpg')
        self.blank = np.zeros(self.img.shape, dtype='uint8')

    def create_contours(self):
        self.numpy_points = np.array([self.points])

        cv.drawContours(self.blank, self.numpy_points, -1, (255,255,255), thickness = -1)

        self.copy = self.img.copy()
        alpha = .5
        mask = self.blank.astype(bool)
        self.copy[mask] = cv.addWeighted(self.img, alpha, self.blank, 1 - alpha, 0)[mask]

        # print(self.img.shape)

    def input_text(self):
        
        textSize, baseline = cv.getTextSize(self.text, cv.FONT_HERSHEY_COMPLEX, 1.0, thickness = 3)
        textSizeWidth, textSizeHeight = textSize
        print(f'text width is {textSizeWidth} pixels')
        print(f'text height is {textSizeHeight} pixels')

        if self.h >= textSizeHeight+10 and self.w >= textSizeWidth+10:
            cv.putText(self.copy, self.text, (self.points[3][0]+5,self.points[3][1]-5), cv.FONT_HERSHEY_COMPLEX, 1.0, (255,1,1), thickness= 2)
            
        else: # changes box to red and prints "text is too big" when the text doesn't fit into the box
            cv.drawContours(self.blank, self.numpy_points, -1, (1,1,255), thickness = -1)

            self.copy = self.img.copy()
            alpha = .5
            mask = self.blank.astype(bool)
            self.copy[mask] = cv.addWeighted(self.img, alpha, self.blank, 1 - alpha, 0)[mask]

            cv.putText(self.copy, "Box is not big enough to fit text", (100, 200), cv.FONT_HERSHEY_COMPLEX, 1.0, (1,1,255), thickness = 3)

        # cv.putText(self.copy, "simplex", (100,400), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), thickness = 2)
        # cv.putText(self.copy, "comp_small", (100,500), cv.FONT_HERSHEY_COMPLEX_SMALL, 1.0, (1,1,255), thickness = 2)
        # cv.putText(self.copy, "duplex", (300,400), cv.FONT_HERSHEY_DUPLEX, 1.0, (1,1,255), thickness = 2)
        # cv.putText(self.copy, "plain", (300,500), cv.FONT_HERSHEY_PLAIN, 1.0, (0,0,255), thickness = 2)
        # cv.putText(self.copy, "script_comp", (500,400), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (0,0,255), thickness = 2)
        # cv.putText(self.copy, "script_simp", (500,500), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 1.0, (0,0,255), thickness = 2)
        # cv.putText(self.copy, "complex", (700,400), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), thickness = 2)

        cv.imshow('tokyo', self.copy)
        cv.imshow('blank', self.blank)

    def text_with_box (self, string, top_right_coords):
        img = self.img.copy()
        blank = self.blank.copy()

        textSize, baseline = cv.getTextSize(string, cv.FONT_HERSHEY_COMPLEX, 1.0, thickness = -1)
        w, h = textSize
        
        x, y = top_right_coords
        points = [[x,y], [x+w+10,y], [x+w+10, y+h+10], [x,y+h+10]]
        points = np.array([points])
        cv.drawContours(blank, points, -1, (255,255,255), thickness = -1)
        
        y += h + 5
        x += 5

        image_copy = img.copy()
        alpha = .4
        mask = blank.astype(bool)
        image_copy[mask] = cv.addWeighted(img, alpha, blank, 1 - alpha, 0)[mask]

        cv.putText(image_copy, string, (x,y), cv.FONT_HERSHEY_COMPLEX, 1.0, (255,1,1), thickness = 2)

        cv.imshow('blank', blank)
        cv.imshow('img', image_copy)

top_left = [100,100]
h = 40
w = 200
box_string = "MARIN"
box_one = Create_Contours_and_Text(box_string, top_left, h, w)

# box_one.create_contours()
# box_one.input_text()

box_one.text_with_box("YOSHIAKI HELLO", (100, 250))

cv.waitKey(0)