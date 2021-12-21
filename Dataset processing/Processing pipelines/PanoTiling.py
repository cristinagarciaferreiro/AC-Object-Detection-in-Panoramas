# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 11:20:26 2021
@author: Cris
Adapted from John Kufuor
"""

import numpy as np
import cv2
import os
import glob
from random import *


# Opens a image in RGB mode
def tile(path):
    for file in glob.glob(path + '/*.jpg'):
        print('got the file')
        filename = os.path.basename(file).split('.')[0]
        print("the file name is ",filename)
        im = cv2.imread(file)
        height, width, channels = im.shape
        w = int(width/4)
        h = int(height/2)
        for z in range(0,1):
            for i in range(0,3):
                y=int(h*z+h/2)
                x=int(w*i+w/2)
                crop = im[y:y+h, x:x+w]
                print('cut the file')
                #cv2.imwrite('{}-{}{}.jpg'.format(file[-12:-4], i, z), crop)
                cv2.imwrite(filename+'CutIn3'+'_z'+str(z)+'_i'+str(i)+'_randomiser'+str(randint(1,10000000))+'.jpg', crop)
        for z in range(0,1):
            for i in range(0,4):
                y=int(h*z+h/2)
                x=int(w*i)
                crop = im[y:y+h, x:x+w]
                print('cut the file')
                #cv2.imwrite('{}-{}{}.jpg'.format(file[-12:-4], i, z), crop)
                cv2.imwrite(filename+'CutIn4'+'_z'+str(z)+'_i'+str(i)+'_randomiser'+str(randint(1,10000000))+'.jpg', crop)
        for z in range(0,2):
            for i in range(0,3):
                y=int(h*z)
                x=int(w*i+w/2)
                crop = im[y:y+h, x:x+w]
                print('cut the file')
                #cv2.imwrite('{}-{}{}.jpg'.format(file[-12:-4], i, z), crop)
                cv2.imwrite(filename+'CutIn6'+'_z'+str(z)+'_i'+str(i)+'_randomiser'+str(randint(1,10000000))+'.jpg', crop)
        for z in range(0,2):
            for i in range(0,4):
                y=int(h*z)
                x=int(w*i)
                crop = im[y:y+h, x:x+w]
                print('cut the file')
                #cv2.imwrite('{}-{}{}.jpg'.format(file[-12:-4], i, z), crop)
                cv2.imwrite(filename+'CutIn8'+'_z'+str(z)+'_i'+str(i)+'_randomiser'+str(randint(1,10000000))+'.jpg', crop)

image_path = 'C:/Users/anton/Desktop/Datasets/PanoSliding'
tile(image_path)