

import cv2 as cv 
import numpy as np 
import matplotlib.pyplot as plt

# img=cv.imread("deep_learning/OpenCV/gray_scale_image.jpeg",0)

# ret,thresh1= cv.threshold(img,150,255,cv.THRESH_BINARY)
# ret,thresh2= cv.threshold(img,150,255,cv.THRESH_BINARY_INV)
# ret,thresh3= cv.threshold(img,150,255,cv.THRESH_TRUNC)
# ret,thresh4= cv.threshold(img,150,255,cv.THRESH_TOZERO_INV)


# cv.imshow("original",img)
# cv.imshow("thsesh_binary",thresh1)
# cv.imshow("thsesh_binry_Inv",thresh2)
# cv.imshow("thsesh_trunk",thresh3)
# cv.imshow("thsesh_tozero",thresh4)

# cv.waitKey(0)
# cv.destroyAllWindows()

# adaptive thresholding

# img=cv.imread("deep_learning/OpenCV/suduko_image.png",0)

# # (img,maximu value,adaptive method,threshold type,neibourhood pixels,constant)

# ret, thresh2=cv.threshold(img,150,255,cv.THRESH_BINARY)
# thresh1= cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,77,5)


# cv.imshow('original',img)
# cv.imshow('adptive',thresh1)
# cv.imshow('simple',thresh2)

# cv.waitKey(0)
# cv.destroyAllWindows()

# otsu thresholding

img=cv.imread("deep_learning/OpenCV/otsu_images.jpeg")

# cv.imshow("original",img)
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

ret,thresh1= cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU )

cv.imshow("gray",gray)
cv.imshow("Otsu",thresh1)
print(ret)

hist=cv.calcHist([gray],[0], None,[256],[0,256])
plt.plot(hist)
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()

