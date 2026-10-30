
import matplotlib.pyplot as plt
import cv2 as cv

import numpy as np

# img=cv.imread("deep_learning/OpenCV/sample.webp")
# cv.imshow('Img',img)
# cv.imwrite("sample.webp",img)

# cv.waitKey(3000)
# cv.destroyAllWindows()

# Binary img
# img1=cv.imread("deep_learning/OpenCV/sample.webp",0)
# cv.imshow("binary",img1)
# print(img1)

# print(type(img1))
# print(img1.shape)
# print(img1.dtype)
# print(img1.size)
# cv.waitKey(3000)
# cv.destroyAllWindows()

# grayscale image

# img2=cv.imread("deep_learning/OpenCV/gray_scale_image.jpeg",0)
# cv.imshow("Gray_scale_Image",img2)
# print(type(img2))

# print(img2.shape)
# print(img2.dtype)
# print(img2.size)
# print(img2)
# cv.waitKey(3000)
# cv.destroyAllWindows()

# color image---------------
# img=cv.imread("deep_learning/OpenCV/color_images.jpeg",1)
# cv.imshow("color_iMage",img)
# print(type(img))

# print(img.shape)
# print(img.dtype)
# print(img.size)
# print(img)
# cv.waitKey(3000)
# cv.destroyAllWindows()

# creating using numpy array ,Black Image
# img1=np.zeros((500,500),dtype=("uint8"))
# cv.imshow("Black",img1)

# img2=np.ones((500,500),dtype="uint8")*255
# cv.imshow("White",img2)



# img3=np.ones((500,500),dtype="uint8")*150
# cv.imshow("grey",img3)

# cv.waitKey(3000)
# cv.destroyAllWindows()


# modify pixel
# img=cv.imread('deep_learning/OpenCV/color_images.jpeg')
# px=img[100,150,0]
# print(px)
# blu_val=img[100,150,0]
# print(blu_val)
# img[15:80,95:150]=(255,0,0)
# img[15:80,95:150]=(0,255,0)
# img[15:80,95:150]=(0,0,255)

# plt.imshow(img)
# plt.show()

# cv.waitKey(0)
# cv.destroyAllWindows()

# ------------cropping one exact position-------

# img=cv.imread('deep_learning/OpenCV/color_images.jpeg')
# img1=img[10:80,100:175]
# cv.imshow("head",img1)
# cv.waitKey(0)
# cv.destroyAllWindows()

# ----------split images--------
# img=cv.imread("deep_learning/OpenCV/color_images.jpeg")
# # cv.imshow("Image",img)

# b,g,r=cv.split(img)

# # cv.imshow("Blue",b)
# # cv.imshow("Green",g)
# # cv.imshow("Red",r)

# # ---------image Merge channel -----------
# img2=cv.merge((b,g,r))
# cv.imshow("Merged",img2)

# cv.waitKey(0)
# cv.destroyAllWindows()

# ----------convert color spaces----------

# img=cv.imread("deep_learning/OpenCV/color_images.jpeg")
# cv.imshow("Image",img)

# ------changing color spaces------

# changing color to grayscale
# img1=cv.cvtColor(img,cv.COLOR_BGR2GRAY) 
# # changing to color hsv
# img2=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# # chnaging to rgb
# img3=cv.cvtColor(img,cv.COLOR_BGR2RGB)

# cv.imshow("gray",img1)
# cv.imshow("HSV",img2)
# cv.imshow("RGB",img3)

# cv.waitKey(0)
# cv.destroyAllWindows()

# -------resize an Image-------
# img=cv.imread("deep_learning/OpenCV/color_images.jpeg")
# cv.imshow("image",img)
# print(img.shape)

# scale=50
# width=int(img.shape[1]*scale/100)
# height=int(img.shape[0]*scale/100)

# dim= (width,height)

# downscale
# Same procedure,only the difference is the scale value should be greater than 100 

# img1=cv.resize(img,dim, interpolation=cv.INTER_AREA)


# cv.imshow("downscaled",img1)
# cv.waitKey(8000)
# cv.destroyAllWindows()

# upscaling
# img=cv.imread("deep_learning/OpenCV/color_images.jpeg")
# cv.imshow("image",img)
# print(img.shape)

# scale=150
# width1=int(img.shape[0]*scale/100)
# height1=int(img.shape[1]*scale/100)

# dim1=(width1,height1)

# img2=cv.resize(img,dim1,interpolation=cv.INTER_AREA)
# cv.imshow("upscaled",img2)

# cv.waitKey(8000)
# cv.destroyAllWindows()

# width only change
img=cv.imread("")
cv.imshow("Image",img)
print(img.shape)

# width=500
# height=int(img.shape[0])
# width=int(img.shape[1])
# height=500
# custom size width,height--


