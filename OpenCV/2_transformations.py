import cv2 as cv

## 1. IMAGES TRANSFORMATION
import numpy as np

img = cv.imread('Pictures/wolfcolor.jpg')

# 1.1 Translation funtion 

def translate(img, x, y):
    # -x: left shift, +x: right shift --> X coordinate to translate to
    # -y: shift up, +y:shift up ---> Y coordina to translate to
    
    transmatrix = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    
    return cv.warpAffine(img, transmatrix, dimensions)

    #Applying image translation 
    
translated = translate(img, 100, 100)
#cv.imshow('Translated', translated)


# 3.2 Rotation funtion

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:  #Defining rotation point
        rotPoint = (width//2, height//2)
    
    rotmatrix = cv.getRotationMatrix2D(rotPoint, angle, scale=1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotmatrix, dimensions)

    #Applying rotation
    
rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)


# 2.3 Flipping
#1: Vertically, 0: Horizontally, -1: Both
flipped = cv.flip(img, 1)
cv.imshow('Flipped', flipped)
cv.waitKey(0)

## 2. BASIC IMAGE FUNCTIONS

## Passing kernels to the images would represent a
## potential improvement or deterioration for the edge detection

img = cv.imread('Pictures/wolfcolor.jpg')
cv.imshow('Original', img)

#Converting to gray
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray_img)

#Bluring - Gaussian 
blur_img = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur_img)

#Edge cascade
canny = cv.Canny(blur_img, 125, 175) #passing a blured image would give less edges
cv.imshow('canny', canny)

# Dilating image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (7,7), iterations=2)
cv.imshow('eroded', eroded)

#Cropping
cropped = img[100:400, 300:500]
cv.imshow('Cropped', cropped)

cv.waitKey(0)