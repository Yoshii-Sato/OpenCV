import  cv2 as cv

img = cv.imread('Photos/dwayne.jpg')
cv.imshow('Group', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray robert', gray)


haar_cascade = cv.CascadeClassifier('haar_face.xml')
# stored the code into this variable
# this is the stored variable

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
# rectangle coordinates of the face
# give me a chance, give me a chance

print(f'Numbers of faces found = {len(faces_rect)}')
print(faces_rect)

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

circle = cv.circle(img, (266, 95), 20, (255,0,0), 3)
cv.imshow('circle', circle)

cv.imshow('Detected Faces', img)

cv.waitKey(0)