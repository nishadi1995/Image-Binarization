import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('Cameraman.png',0)

#plotting the histogram
plt.hist(img.ravel(),256,[0,256])
plt.title('Input image histogram')
plt.show()

ret,thresh1 = cv.threshold(img,20,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,40,255,cv.THRESH_BINARY)
ret,thresh3 = cv.threshold(img,80,255,cv.THRESH_BINARY)
ret,thresh4 = cv.threshold(img,100,255,cv.THRESH_BINARY)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_BINARY)

titles = ['Original Image','T=20','T=40','T=80','T=100','T=127']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()
