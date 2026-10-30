


import cv2 as cv 

img=cv.imread("deep_learning/OpenCV/color_images.jpeg")


cv.imshow("Image",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray_image",gray)
width=400
height=300

dim=(width,height)
img1=cv.resize(gray,dim,interpolation=cv.INTER_AREA)
cv.imshow("resized",img1)



