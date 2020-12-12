#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:34:02 2020

@author: ritadang
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img3=mpimg.imread('/Users/ritadang/Desktop/PIC 16/HW5/g.jpg')
img4=mpimg.imread('/Users/ritadang/Desktop/PIC 16/HW5/h.jpg')


#img4-img3 gives the differences between the 2 images
#.astype(int) turns the data type into signed numbers
#abs() makes all numbers positive
imgdiff=abs(img4-img3.astype(int)) 
#int is a more powerful data type, so when one of them has type int, the resulting matrix will have type int

plt.imshow(imgdiff)
plt.show()
mpimg.imsave('i.jpg',imgdiff.astype(np.uint8))  #save the image to i.jpg
