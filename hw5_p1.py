#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 22:42:03 2020

@author: ritadang
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#load the 2 images
img1=mpimg.imread('/Users/ritadang/Desktop/PIC 16/HW5/a.jpg')
img2=mpimg.imread('/Users/ritadang/Desktop/PIC 16/HW5/b.jpg')


#print(img1.shape)
#print(img2.shape)

#plt.imshow(img1)
#plt.imshow(img1)

imgc=img1.copy()
imgc[250:650,100:500,:]=img2[:]  #array slicing

plt.imshow(imgc)
plt.show()

#save image to c.jpg
mpimg.imsave('c.jpg',imgc)