

import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

img=cv.imread("deep_learning/OpenCV/color_images.jpeg",0)

cv.imshow("image",img)
hist=cv.calcHist([img],[0],None,[256],[0,255])

plt.plot(hist)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()