import cv2 as cv
from cv2 import resize

# 1. Reading images and videos

# #1.1 Images
# img = cv.imread('Pictures/wolf.jpg')

# cv.imshow('wlf', img)
# cv.waitKey(0)


#1.2 Videos
capture = cv.VideoCapture('Videos/EquinorBrand.mp4')

# reaidng video frame by frame 
while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame)

    #breaking our video play
    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.realease()
cv.destroyAllWindows()
    
    
    
### ----------------------------



#2. Reacaling frames funtion 
def rescaleFrame(frame, scale=0.75):
    
    """ works for existing image and video files but no for live videos """
    
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimentions = (width, height)
    
    return cv.resize(frame, dimentions, interpolation=cv.INTER_LINEAR)

# #2.1 plotting original and rescaled images
# img = cv.imread('Pictures/wolf.jpg')
# img_rescaled = rescaleFrame(img, 0.5)

# cv.imshow('wlf_rescaled', img_rescaled)
# cv.imshow('wlf', img)
# cv.waitKey(0)


#2.2 plotting original and rescaled video
capture = cv.VideoCapture('Videos/EquinorBrand.mp4')

# reaidng video frame by frame 
while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame, 0.25)
    
    cv.imshow('Video', frame) #originalvide
    cv.imshow('RescaledVideo', frame_resized) #rescaled video
    
    #breaking our video play
    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.realease()
cv.destroyAllWindows()