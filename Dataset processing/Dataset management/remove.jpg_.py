# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 2021

@author: Cris

Adapted from https://www.reddit.com/r/learnpython/comments/2yayel/how_to_remove_part_of_a_file_name_recursively_in/
"""

import glob
import os

images_path = 'C:/Users/anton/Desktop/Datasets/PanosTiled/test480'


for img in glob.glob(images_path + '/*.jpg'):
    path, file_name = os.path.split(img)
    new_name = file_name.replace(' ', '')
    new_path = os.path.join(path, new_name)
    os.rename(img, new_path)
    
for img in glob.glob(images_path + '/*.txt'):
    path, file_name = os.path.split(img)
    new_name = file_name.replace(' ', '')
    new_path = os.path.join(path, new_name)
    os.rename(img, new_path)
