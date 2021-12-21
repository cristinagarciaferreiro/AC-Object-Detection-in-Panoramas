# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:17:52 2021

@author: anton

https://python.plainenglish.io/automatically-resize-all-your-images-with-python-36f5b6dfc275
"""

import cv2
import os

def resizeImg(image, width=None, height=None):
  dim=None
  (h,w) = image.shape[:2]
  if width is None and height is None:
    return image
  
  elif width is not None and height is not None:
    dim = (width, height)
  
  elif width is None:
    r = height/float(h)
    dim = (int(w*r), height)
  else:
    r = width / float(w)
    dim = (width, int(h*r))
  resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
  return resized

def main():
  folder = "C:/Users/anton/Desktop/Datasets/Boan+Cubes+BoanSwitchesSockets/trainBoan+Cubes+SwitchesSockets"
  newResizedFolder = "C:/Users/anton/Desktop/Datasets/Boan+Cubes+BoanSwitchesSockets"
  for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder, filename))
    if img is not None:
      newImage = resizeImg(img, 480, None) #we'll fill in this later
      newImgPath = filename
      cv2.imwrite(newImgPath, newImage)
if __name__ == "__main__":
  main()