import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


cap=cv.VideoCapture(0)

while True:
    ret,frame=cap.read()

    if not ret:
        print('cannot connect')
        break

    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    cv.putText(frame,'Open CV',(100,100),cv.FONT_HERSHEY_COMPLEX,1 ,(0,0,0),3)
    cv.imshow('video', frame)
    cv.imshow('video1', gray)
    cv.imshow('video2', hsv)


    if cv.waitKey(1) == ord('h'):
        break


cv.destroyAllWindows()
