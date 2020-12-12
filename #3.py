#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:46:53 2020

@author: ritadang
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img5=mpimg.imread('/Users/ritadang/Desktop/PIC 16/HW5/e.jpg')
img6=mpimg.imread('/Users/ritadang/Desktop/PIC 16/HW5/d.jpg')

#plt.imshow(img5)

#Replace the green background with black background
mask=np.logical_and(img5[:,:,0]<20, img5[:,:,1]>230)
img5c=img5.copy()
img5c[mask]=0

plt.imshow(img5c)
plt.show()
mpimg.imsave('d.jpg',img5c)

#plt.imshow(img6)

#Place the minion in f.jpg
img5copy=img5c.copy()
maskblack=img5copy==0
img6c=img6.copy()
img6cut=img6[559:720,265:430,:]  #get the overlapping section
img5copy[maskblack]=img6cut[maskblack]  #replace the black background
img6c[559:720,265:430,:]=img5copy[:]


plt.imshow(img6c)
plt.show()
mpimg.imsave('f.jpg',img6c)
