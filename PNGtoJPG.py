# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 19:03:08 2021

@author: anton

Adapted from https://stackoverflow.com/questions/60048149/converting-png-to-jpg-in-python
"""

import cv2
import glob
import os

images_path = 'C:/Users/anton/Downloads/trainBoan+Cubes+SwitchesSockets'
    
for img in glob.glob(images_path + '/*.png'):
    path, file_name = os.path.split(img)
    print(file_name)
    # Load .png image
    image = cv2.imread(img)
    # Save .jpg image
    # cv2.imwrite(str(file_name) +'.jpg', image)
    cv2.imwrite(img[:-3] + 'jpg', image)
    os.remove(img[:-3] + 'png')