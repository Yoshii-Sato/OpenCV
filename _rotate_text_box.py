import cv2 as cv
import numpy as np

img = cv.imread('Photos/tokyo.jpg')

def create_coords_of_rotated_rectangle(top_left, angle, h, w):
    '''returns the 4 edge coordinates of a rectangle rotated a certain amount of degrees (in relation to top left corner)
    :also returns a bool value that is true when the box is good, false when either non-applicable or out-of-bounds
    
    '''
    x, y = top_left
    x_2 = x+w*np.cos(np.radians(angle))
    y_2 = y-w*np.sin(np.radians(angle))
    x_3 = x+w*np.cos(np.radians(angle))+h*np.cos(np.radians(90-angle))
    y_3 = y-w*np.sin(np.radians(angle))+h*np.sin(np.radians(90-angle))
    x_4 = x+h*np.cos(np.radians(90-angle))
    y_4 = y+h*np.sin(np.radians(90-angle))

    points = [[x,y],[round(x_2),round(y_2)],[round(x_3), round(y_3)],[round(x_4),round(y_4)]]
    print(f'the coords of the rectangle are: {points}')

    h = img.shape[0]
    w = img.shape[1]

    if (x <= w and x >= 0) and (x_2 <= w and x_2 >= 0) and (x_3 <= w and x_3 >= 0) and (x_4 <= w and x_4 >= 0) and (y <= w and y >= 0) and (y_2 <= w and y_2 >= 0) and (y_3 <= w and y_3 >= 0) and (y_4 <= w and y_4 >= 0):
        print('''Your coords look fine!
        ''')
        return points, True  
    else:
        print('''one or more of your points are out of boundary
        
        
        ---------fix now---------
        ''')
        # hi
        points = [[0,0],[img.shape[1], img.shape[0]],[img.shape[1], 0],[0, img.shape[0]]]
        return points, False

def draw_contours(img, points, reverse = True):
    points = np.array([points])
    if reverse:
        cv.drawContours(img, points, -1, (255,255,255), thickness= 2)
    else:
        cv.drawContours(img, points, -1, (0,0,255), thickness= 2)
        cv.putText(img, "contours not good enough", (50, img.shape[0]//2 + 11), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,0,255), thickness = 2)

def find_rotated_angle_of_box(points):
    delta_y = points[1][1] - points[0][1]
    delta_x = points[1][0] - points[0][0]

    alpha = np.degrees(np.arctan(delta_y/delta_x))

    if abs(alpha) > 45:
        if alpha >= 0:
            alpha -= 90
        elif alpha < 0:
            alpha += 90

    return alpha

def rotate_image(mat, angle):
    '''creates the rotation matrix of the image whilest not cutting off the edges of the shape
    then creates an image with the rotation matrix and the newly created dimensions of the larger image
    '''
    height, width = mat.shape[:2]
    image_center = (width/2, height/2) #center of the image

    rotation_mat = cv.getRotationMatrix2D(image_center, angle, 1.)

    # rotation calculates the cos and sin, taking absolutes of those.
    abs_cos = abs(rotation_mat[0,0]) 
    abs_sin = abs(rotation_mat[0,1])

    # find the new width and height bounds
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    # subtract old image center (bringing image back to origo) and adding the new image center coordinates
    rotation_mat[0, 2] += bound_w/2 - image_center[0]
    rotation_mat[1, 2] += bound_h/2 - image_center[1]

    rotated_mat = cv.warpAffine(mat, rotation_mat, (bound_w, bound_h))
    return rotated_mat, rotation_mat

def get_new_rotated_coords(point, rotation_matrix):
    x,y = point
    x_rotated, y_rotated = np.dot(rotation_matrix, np.array([x,y,1]))
    coords = (round(x_rotated), round(y_rotated))

    return coords

def put_text_inside_box(img, text, top_left_coords, reverse = True):
    if reverse:   
        x, y = top_left_coords
        
        textSize, baseline = cv.getTextSize(text, cv.FONT_HERSHEY_COMPLEX, 1.0, thickness = 2)
        textWidth, textHeight = textSize
        cv.putText(img, text, (x+5, y+textHeight+5), cv.FONT_HERSHEY_COMPLEX, 1.0, (255,0,0), thickness= 2)

def unrotate_rotated_img(img_width, img_height, angle):
    """Returns 2x3 rotation matrix for the given rotation angle and image
    dimensions, and considers image borders expansion.

    :param img_width: image width
    :type img_width: int
    :param img_height: image height
    :type img_height: int
    :param angle: rotation angle in degrees
    :type angle: float
    :return: 2x3 rotation matrix
    :rtype: np.ndarray
    """

    abs_cos = abs(np.cos(np.radians(angle)))
    abs_sin = abs(np.sin(np.radians(angle)))

    expanded_width = int(img_height * abs_sin + img_width * abs_cos)
    expanded_height = int(img_height * abs_cos + img_width * abs_sin)

    rotation_matrix = cv.getRotationMatrix2D((expanded_width / 2, expanded_height / 2), -angle, 1)
    rotation_matrix[0, 2] -= (expanded_width - img_width) / 2
    rotation_matrix[1, 2] -= (expanded_height - img_height) / 2
    
    return cv.warpAffine(rotated_img, rotation_matrix, (img.shape[1], img.shape[0]))

# artificially enters box

points, okay = create_coords_of_rotated_rectangle((100,300), angle = 30, h = 70, w = 400)

# draws box contours with points on the image
draw_contours(img, points, okay)

cv.imshow('img', img)

# gets the rotated image and its matrix using the angle that the box was rotated
rotated_img, rotation_matrix = rotate_image(img, angle = find_rotated_angle_of_box(points))

# puts text inside the box using the new coordinates of the box on rotated image
put_text_inside_box(rotated_img, "YOSHIBOTO RABBIT", top_left_coords= get_new_rotated_coords(points[0], rotation_matrix), reverse = okay)

# unrotates the rotated image
unrotated_img = unrotate_rotated_img(img.shape[1],img.shape[0], angle= find_rotated_angle_of_box(points)) 

cv.imshow('rotated image', rotated_img)
cv.imshow('unrotated image', unrotated_img)

cv.waitKey(0)