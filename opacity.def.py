import pyshine as ps
import cv2 as cv
import time
image = cv.imread('Photos/dog_small.jpg')


text  =  'ID: '+str(123)
image = ps.putBText(image,text,text_offset_x=20,text_offset_y=20,vspace=10,hspace=10, font_scale=1.0,background_RGB=(228,225,222),text_RGB=(1,1,1))
text = str(time.strftime("%H:%M %p"))
image = ps.putBText(image,text,text_offset_x=image.shape[1]-170,text_offset_y=20,vspace=10,hspace=10, font_scale=1.0,background_RGB=(228,225,222),text_RGB=(1,1,1))

text  =  '6842'
image = ps.putBText(image,text,text_offset_x=80,text_offset_y=372,vspace=10,hspace=10, font_scale=1.0,background_RGB=(228,225,222),text_RGB=(255,255,255))

text  =  "Lena Fors'en"
image = ps.putBText(image,text,text_offset_x=80,text_offset_y=425,vspace=20,hspace=10, font_scale=1.0,background_RGB=(20,210,4),text_RGB=(255,255,255))

text  =  'Status: '
image = ps.putBText(image,text,text_offset_x=image.shape[1]-130,text_offset_y=200,vspace=10,hspace=10, font_scale=1.0,background_RGB=(228,225,222),text_RGB=(255,255,255))
text  =  'On time'
image = ps.putBText(image,text,text_offset_x=image.shape[1]-130,text_offset_y=242,vspace=10,hspace=10, font_scale=1.0,background_RGB=(228,225,222),text_RGB=(255,255,255))


text  =  'Attendence: '
image = ps.putBText(image,text,text_offset_x=image.shape[1]-200,text_offset_y=394,vspace=10,hspace=10, font_scale=1.0,background_RGB=(228,225,222),text_RGB=(255,255,255))
text  =  '96.2%      '
image = ps.putBText(image,text,text_offset_x=image.shape[1]-200,text_offset_y=436,vspace=10,hspace=10, font_scale=1.0,background_RGB=(228,225,222),text_RGB=(255,255,255))

cv.imshow('Output', image)
cv.imwrite('out.jpg',image)
cv.waitKey(0)