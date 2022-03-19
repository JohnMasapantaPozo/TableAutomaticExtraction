import cv2 as cv
from cv2 import FONT_HERSHEY_COMPLEX
import numpy as np

# 1. create an blank image to draw in

blank = np.zeros((500, 500, 3), dtype='uint8')
#cv.imshow('blank', blank)

# # 2. paint the imnnage with a color

# #blank[150:200, 400:500] = 255, 0, 0 #only one square in blue
# blank[:] = 255, 0, 0  # all in blue
# cv.imshow('Green', blank)

# 3. draw a rectangule

cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness=5) #to fill thickness=-1
#cv.imshow('rect', blank)

# 4. draw circle
cv.circle(blank, (250, 250), 25, (0,0,255), thickness=-1)
# cv.imshow('circle', blank)

# 5. draw line
cv.line(blank, (0,0), (250, 250), (255, 255, 255), thickness=4)
cv.imshow('line', blank)

# 6. text

cv.putText(blank, 'Hello', (255, 255), fontFace=FONT_HERSHEY_COMPLEX, fontScale=FONT_HERSHEY_COMPLEX ,color = (255, 255, 255), thickness=3)
cv.imshow('text', blank)

# img = cv.imread('Pictures/wolf.jpg')
# cv.imshow('wlf', img)

cv.waitKey(0)