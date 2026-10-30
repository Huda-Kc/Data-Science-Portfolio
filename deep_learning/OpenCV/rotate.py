

import cv2 as cv
import numpy as pd
import matplotlib.pyplot as plt


img=cv.imread("deep_learning/OpenCV/sample.webp")


# -------rotate imge-------
# img1=cv.rotate(img,cv.ROTATE_90_CLOCKWISE)
# cv.imshow("90clockwise",img1)

# img2=cv.rotate(img,cv.ROTATE_180)
# cv.imshow("180 clockwise",img2)

# img3=cv.rotate(img,cv.ROTATE_90_COUNTERCLOCKWISE)
# cv.imshow("90_counter_clockwise",img3)

# cv.waitKey(0)
# cv.destroyAllWindows()

# coustom rotation
# rows,cols,channel=img.shape
# center=(cols/2,rows/2)
# print(center)
# M=cv.getRotationMatrix2D(center=center,angle=45,scale=1)
# img4=cv.warpAffine(img,M,(cols,rows))
# cv.imshow("roteated5",img4)
# cv.waitKey(0)
# cv.destroyAllWindows()

# add text to image

# cv.putText(img,'Learn Open CV Python',(200,400),cv.FONT_HERSHEY_COMPLEX,1,(0,0,255),3)
# # 100,100 - eath pointil ninnan thudaggendayth enna,1-scale,0,0,255-is a red colr,3-means thickness

# cv.imshow("flower",img)

# img1=plt.imread("deep_learning/OpenCV/sample.webp")
# plt.imshow(img1)
# plt.show()
# cv.waitKey(0)
# cv.destroyAllWindows()


