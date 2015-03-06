# -*- coding: utf-8 -*-
"""
Created on Fri Mar 06 15:35:49 2015

@author: ahopkins
"""
from class_vis import output_image
output_image("test.png", "png", open("test.png", "rb").read())

#import matplotlib.pylab as plt
#plt.ion()
#plt.plot([1,2,3])
#plt.show()
#plt.ylabel('This is an axis')
#print ("Hello")