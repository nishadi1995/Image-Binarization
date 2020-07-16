import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('input2.png',0)
img = cv.medianBlur(img,5)

blur = cv.GaussianBlur(img,(5,5),0)

th1 = cv.adaptiveThreshold(blur,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)

ret2,th2 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

titles = ['Original Noisy Image', 'Gaussian Filtered Image','Adaptive Mean Thresholding', 'Otsu Thresholding']
images = [img, blur,th1, th2]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
