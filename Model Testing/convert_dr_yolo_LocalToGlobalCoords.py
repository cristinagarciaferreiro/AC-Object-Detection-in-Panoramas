# -*- coding: utf-8 -*-
"""
Adapted from
https://github.com/Cartucho/mAP
"""

import os
import re
import cv2
import numpy as np
import matplotlib.pyplot as plt

# make sure that the cwd() in the beginning is the location of the python script (so that every path makes sense)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

IN_FILE = 'C:/Users/anton/Desktop/mAP-master/scripts/extra/resultKikeKripis23.txt'

# change directory to the one with the files to be changed
parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
parent_path = os.path.abspath(os.path.join(parent_path, os.pardir))
DR_PATH = os.path.join(parent_path, 'input','detection-results')
#print(DR_PATH)
os.chdir(DR_PATH)

# Set the SEPARATOR_KEY equal to the images_path on ModelOnPython
SEPARATOR_KEY = '/content/gdrive/MyDrive/FasterRCNN2/dataset/test/'
IMG_FORMAT = '.jpg'

outfile = None
with open(IN_FILE) as infile:
    for line in infile:
        if SEPARATOR_KEY in line:
            if IMG_FORMAT not in line:
                break
            # get text between two substrings (SEPARATOR_KEY and IMG_FORMAT)
            image_path = re.search(SEPARATOR_KEY + '(.*)' + IMG_FORMAT, line)
            # get the image name (the final component of a image_path)
            # e.g., from 'data/horses_1' to 'horses_1'
            image_name = os.path.basename(image_path.group(1))
            # close the previous file
            if outfile is not None:
                outfile.close()
            # open a new file
            print("image name is ",image_name)
            outfile = open(os.path.join(DR_PATH, image_name + '.txt'), 'w')
        elif outfile is not None:
            # Get i and z values
            iSearch = re.search("_i" + '(.*)' + "_randomiser", image_name)
            i = os.path.basename(iSearch.group(1))
            zSearch = re.search("_z" + '(.*)' + "_i", image_name)
            z = os.path.basename(zSearch.group(1))
            print("i is ",i, "z is ",z)
            # If CutIn8, newleft=left+480i and newtop=top+480z (conversion local to global coords)
            if("CutIn8" in image_name):
                print("image name contains CutIn8")
                # split line on first occurrence of the character ':' and '%'
                class_name, info = line.split(':', 1)
                print("class name is ",class_name)
                if class_name == "concealed_duct_vent_indoor_hvac":
                    confidence, bbox = info.split('%', 1)
                    # get all the coordinates of the bounding box
                    bbox = bbox.replace(')','') # remove the character ')'
                    # go through each of the parts of the string and check if it is a digit
                    left, top, width, height = [int(s) for s in bbox.split() if s.lstrip('-').isdigit()]
                    newLeft = left + 480*int(i)
                    newTop = top + 480*int(z)
                    right = newLeft + width
                    bottom = newTop + height
                    outfile.write("{} {} {} {} {} {}\n".format(0, float(confidence)/100, newLeft, newTop, right, bottom))
                    print("outputted file with global coords!")
                    #cv2.rectangle(img, pt1=(newLeft,newTop), pt2=(right,bottom), color=(255,0,0), thickness=1)
                    #cv2.imwrite('C:/Users/anton/Desktop/Datasets/PanoSliding/7fzx1.jpg',img)
                elif class_name == "wall_mounted_indoor_hvac":
                    confidence, bbox = info.split('%', 1)
                    # get all the coordinates of the bounding box
                    bbox = bbox.replace(')','') # remove the character ')'
                    # go through each of the parts of the string and check if it is a digit
                    left, top, width, height = [int(s) for s in bbox.split() if s.lstrip('-').isdigit()]
                    newLeft = left + 480*int(i)
                    newTop = top + 480*int(z)
                    right = newLeft + width
                    bottom = newTop + height
                    outfile.write("{} {} {} {} {} {}\n".format(1, float(confidence)/100, newLeft, newTop, right, bottom))
                    print("outputted file with global coords!")
                    #cv2.rectangle(img, pt1=(newLeft,newTop), pt2=(right,bottom), color=(255,0,0), thickness=1)
                    #cv2.imwrite('C:/Users/anton/Desktop/Datasets/PanoSliding/7fzx1.jpg',img)
                elif class_name == "cassettes_indoor_hvac":
                    confidence, bbox = info.split('%', 1)
                    # get all the coordinates of the bounding box
                    bbox = bbox.replace(')','') # remove the character ')'
                    # go through each of the parts of the string and check if it is a digit
                    left, top, width, height = [int(s) for s in bbox.split() if s.lstrip('-').isdigit()]
                    newLeft = left + 480*int(i)
                    newTop = top + 480*int(z)
                    right = newLeft + width
                    bottom = newTop + height
                    outfile.write("{} {} {} {} {} {}\n".format(2, float(confidence)/100, newLeft, newTop, right, bottom))
                    print("outputted file with global coords!")
                    #cv2.rectangle(img, pt1=(newLeft,newTop), pt2=(right,bottom), color=(255,0,0), thickness=1)
                    #cv2.imwrite('C:/Users/anton/Desktop/Datasets/PanoSliding/7fzx1.jpg',img)                    
            # If CutIn6
            if("CutIn6" in image_name):
                print("image name contains CutIn6")
                # split line on first occurrence of the character ':' and '%'
                class_name, info = line.split(':', 1)
                print("class name is ",class_name)
                if class_name == "concealed_duct_vent_indoor_hvac":
                    confidence, bbox = info.split('%', 1)
                    # get all the coordinates of the bounding box
                    bbox = bbox.replace(')','') # remove the character ')'
                    # go through each of the parts of the string and check if it is a digit
                    left, top, width, height = [int(s) for s in bbox.split() if s.lstrip('-').isdigit()]
                    newLeft = left + 480*int(i) + int(480/2)
                    newTop = top + 480*int(z)
                    right = newLeft + width
                    bottom = newTop + height
                    outfile.write("{} {} {} {} {} {}\n".format(0, float(confidence)/100, newLeft, newTop, right, bottom))
                    print("outputted file with global coords!")
                    #cv2.rectangle(img, pt1=(newLeft,newTop), pt2=(right,bottom), color=(255,0,0), thickness=1)
                    #cv2.imwrite('C:/Users/anton/Desktop/Datasets/PanoSliding/7fzx1.jpg',img)                    
                elif class_name == "wall_mounted_indoor_hvac":
                    confidence, bbox = info.split('%', 1)
                    # get all the coordinates of the bounding box
                    bbox = bbox.replace(')','') # remove the character ')'
                    # go through each of the parts of the string and check if it is a digit
                    left, top, width, height = [int(s) for s in bbox.split() if s.lstrip('-').isdigit()]
                    newLeft = left + 480*int(i) + int(480/2)
                    newTop = top + 480*int(z)
                    right = newLeft + width
                    bottom = newTop + height
                    outfile.write("{} {} {} {} {} {}\n".format(1, float(confidence)/100, newLeft, newTop, right, bottom))
                    print("outputted file with global coords!")
                    #cv2.rectangle(img, pt1=(newLeft,newTop), pt2=(right,bottom), color=(255,0,0), thickness=1)
                    #cv2.imwrite('C:/Users/anton/Desktop/Datasets/PanoSliding/7fzx1.jpg',img)                    
                elif class_name == "cassettes_indoor_hvac":
                    confidence, bbox = info.split('%', 1)
                    # get all the coordinates of the bounding box
                    bbox = bbox.replace(')','') # remove the character ')'
                    # go through each of the parts of the string and check if it is a digit
                    left, top, width, height = [int(s) for s in bbox.split() if s.lstrip('-').isdigit()]
                    newLeft = left + 480*int(i) + int(480/2)
                    newTop = top + 480*int(z)
                    right = newLeft + width
                    bottom = newTop + height
                    outfile.write("{} {} {} {} {} {}\n".format(2, float(confidence)/100, newLeft, newTop, right, bottom))
                    print("outputted file with global coords!")
                    #cv2.rectangle(img, pt1=(newLeft,newTop), pt2=(right,bottom), color=(255,0,0), thickness=1)
                    #cv2.imwrite('C:/Users/anton/Desktop/Datasets/PanoSliding/7fzx1.jpg',img)                    
            # If CutIn4
            if("CutIn4" in image_name):
                print("image name contains CutIn4")
                # split line on first occurrence of the character ':' and '%'
                class_name, info = line.split(':', 1)
                print("class name is ",class_name)
                if class_name == "concealed_duct_vent_indoor_hvac":
                    confidence, bbox = info.split('%', 1)
                    # get all the coordinates of the bounding box
                    bbox = bbox.replace(')','') # remove the character ')'
                    # go through each of the parts of the string and check if it is a digit
                    left, top, width, height = [int(s) for s in bbox.split() if s.lstrip('-').isdigit()]
                    newLeft = left + 480*int(i)
                    newTop = top + 480*int(z) + int(480/2)
                    right = newLeft + width
                    bottom = newTop + height
                    outfile.write("{} {} {} {} {} {}\n".format(0, float(confidence)/100, newLeft, newTop, right, bottom))
                    print("outputted file with global coords!")
                    #cv2.rectangle(img, pt1=(newLeft,newTop), pt2=(right,bottom), color=(255,0,0), thickness=1)
                    #cv2.imwrite('C:/Users/anton/Desktop/Datasets/PanoSliding/7fzx1.jpg',img)                    
                elif class_name == "wall_mounted_indoor_hvac":
                    confidence, bbox = info.split('%', 1)
                    # get all the coordinates of the bounding box
                    bbox = bbox.replace(')','') # remove the character ')'
                    # go through each of the parts of the string and check if it is a digit
                    left, top, width, height = [int(s) for s in bbox.split() if s.lstrip('-').isdigit()]
                    newLeft = left + 480*int(i)
                    newTop = top + 480*int(z) + int(480/2)
                    right = newLeft + width
                    bottom = newTop + height
                    outfile.write("{} {} {} {} {} {}\n".format(1, float(confidence)/100, newLeft, newTop, right, bottom))
                    print("outputted file with global coords!")
                    #cv2.rectangle(img, pt1=(newLeft,newTop), pt2=(right,bottom), color=(255,0,0), thickness=1)
                    #cv2.imwrite('C:/Users/anton/Desktop/Datasets/PanoSliding/7fzx1.jpg',img)                    
                elif class_name == "cassettes_indoor_hvac":
                    confidence, bbox = info.split('%', 1)
                    # get all the coordinates of the bounding box
                    bbox = bbox.replace(')','') # remove the character ')'
                    # go through each of the parts of the string and check if it is a digit
                    left, top, width, height = [int(s) for s in bbox.split() if s.lstrip('-').isdigit()]
                    newLeft = left + 480*int(i)
                    newTop = top + 480*int(z) + int(480/2)
                    right = newLeft + width
                    bottom = newTop + height
                    outfile.write("{} {} {} {} {} {}\n".format(2, float(confidence)/100, newLeft, newTop, right, bottom))
                    print("outputted file with global coords!")
                    #cv2.rectangle(img, pt1=(newLeft,newTop), pt2=(right,bottom), color=(255,0,0), thickness=1)
                    #cv2.imwrite('C:/Users/anton/Desktop/Datasets/PanoSliding/7fzx1.jpg',img)                    
            # If CutIn3
            if("CutIn3" in image_name):
                print("image name contains CutIn3")
                # split line on first occurrence of the character ':' and '%'
                class_name, info = line.split(':', 1)
                print("class name is ",class_name)
                if class_name == "concealed_duct_vent_indoor_hvac":
                    confidence, bbox = info.split('%', 1)
                    # get all the coordinates of the bounding box
                    bbox = bbox.replace(')','') # remove the character ')'
                    # go through each of the parts of the string and check if it is a digit
                    left, top, width, height = [int(s) for s in bbox.split() if s.lstrip('-').isdigit()]
                    newLeft = left + 480*int(i) + int(480/2)
                    newTop = top + 480*int(z) + int(480/2)
                    right = newLeft + width
                    bottom = newTop + height
                    outfile.write("{} {} {} {} {} {}\n".format(0, float(confidence)/100, newLeft, newTop, right, bottom))
                    print("outputted file with global coords!")
                    #cv2.rectangle(img, pt1=(newLeft,newTop), pt2=(right,bottom), color=(255,0,0), thickness=1)
                    #cv2.imwrite('C:/Users/anton/Desktop/Datasets/PanoSliding/7fzx1.jpg',img)                    
                elif class_name == "wall_mounted_indoor_hvac":
                    confidence, bbox = info.split('%', 1)
                    # get all the coordinates of the bounding box
                    bbox = bbox.replace(')','') # remove the character ')'
                    # go through each of the parts of the string and check if it is a digit
                    left, top, width, height = [int(s) for s in bbox.split() if s.lstrip('-').isdigit()]
                    newLeft = left + 480*int(i) + int(480/2)
                    newTop = top + 480*int(z) + int(480/2)
                    right = newLeft + width
                    bottom = newTop + height
                    outfile.write("{} {} {} {} {} {}\n".format(1, float(confidence)/100, newLeft, newTop, right, bottom))
                    print("outputted file with global coords!")
                    #cv2.rectangle(img, pt1=(newLeft,newTop), pt2=(right,bottom), color=(255,0,0), thickness=1)
                    #cv2.imwrite('C:/Users/anton/Desktop/Datasets/PanoSliding/7fzx1.jpg',img)                    
                elif class_name == "cassettes_indoor_hvac":
                    confidence, bbox = info.split('%', 1)
                    # get all the coordinates of the bounding box
                    bbox = bbox.replace(')','') # remove the character ')'
                    # go through each of the parts of the string and check if it is a digit
                    left, top, width, height = [int(s) for s in bbox.split() if s.lstrip('-').isdigit()]
                    newLeft = left + 480*int(i) + int(480/2)
                    newTop = top + 480*int(z) + int(480/2)
                    right = newLeft + width
                    bottom = newTop + height
                    outfile.write("{} {} {} {} {} {}\n".format(2, float(confidence)/100, newLeft, newTop, right, bottom))
                    print("outputted file with global coords!")
                    #cv2.rectangle(img, pt1=(newLeft,newTop), pt2=(right,bottom), color=(255,0,0), thickness=1)
                    #cv2.imwrite('C:/Users/anton/Desktop/Datasets/PanoSliding/7fzx1.jpg',img)     
    outfile.close()


"""
Created on Wed Nov 24 16:16:25 2021

2. Deletes empty detection files and detections at the edge of images

"""

import os
import numpy as np
from pathlib import Path
from difflib import SequenceMatcher

dir_path = 'C:/Users/anton/Desktop/mAP-master/input/detection-results'

margin = 2

for root, dirnames, files in os.walk(dir_path, topdown=False):
        for f in files:
            full_name = os.path.join(root, f)
            # if there are no detections in this image, delete detections file (it'll be empty)
            if os.path.getsize(full_name) == 0:
               os.remove(full_name)
            # if a file has multiple detections, convert into one file per detection
            path_full_name = Path(full_name)
            if path_full_name.is_file():
                file = open(full_name,'r')
                with file:
                    lines = file.readlines()
                    if len(lines) > 1:
                        print("more than one row")
                        row_number = 0
                        for line in lines:
                            row_number = row_number + 1
                            newFile_path = str(full_name[:-4]) + 'row' + str(row_number) + '.txt'
                            path = Path(newFile_path)
                            newFile = open(path,"a+")
                            newFile.write(line)
                            newFile.close()
                        file.close()
                        os.remove(full_name)
                # if any of the coordinates in the detections file is a multiple of 240 (object cut at the edge), delete detections file
                if path_full_name.is_file():
                    data = np.loadtxt(full_name)
                    print("loaded ",full_name)
                    print("array is ",data)
                    x1 = int(data[2])
                    y1 = int(data[3])
                    x2 = int(data[4])
                    y2 = int(data[5])
                    print("coords are ",x1,y1,x2,y2)
                    # if confidence below 0.5, delete
                    conf1 = float(data[1])
                    if conf1 < 0.5:
                        filePath = Path(full_name)
                        if filePath.is_file():
                            os.remove(full_name)
                    """
                    if (x1 % 240 == 0 and i != 1) or (y1 % 240 == 0 or x2 % 240 == 0 or y2 % 240 == 0:
                        print(full_name,"detection at the edge")
                        filePath = Path(full_name)
                        if filePath.is_file():
                            os.remove(full_name)
                    """
                    for j in range(0,margin+1):
                        print("j = ",j)
                        if (x1+j) % 240 == 0 or (y1+j) % 240 == 0 or (x2+j) % 240 == 0 or (y2+j) % 240 == 0 or (x1-j) % 240 == 0 or (y1-j) % 240 == 0 or (x2-j) % 240 == 0 or (y2-j) % 240 == 0:
                            if (x1+j) != 0 and (x1-j) != 0 and (y1+j) != 0 and (y1-j) != 0 and (x2+j) != 1920 and (x2-j) != 1920 and (y2+j) != 960 and (y2-j) != 960:
                                print(full_name,"detection almost at the edge")
                                filePath = Path(full_name)
                                if filePath.is_file():
                                    os.remove(full_name)
                    

"""
Created on Thu Nov 25 11:09:44 2021

3. Compares files for similarity and deletes files that are very similar

Check the margin and similarityMargin!
"""

import os
import numpy as np
import re
from pathlib import Path
from difflib import SequenceMatcher

dir_path = 'C:/Users/anton/Desktop/mAP-master/input/detection-results'
#number of pixels difference considered the same detection
similarityMargin = 50

# if two detections are two similar, delete the one with the lowest confidence
for root, dirnames, files in os.walk(dir_path, topdown=False):
        for file in files:
            full_name_current = os.path.join(root, file)
            #print("full_name_current is ",full_name_current)
            name_current_search = re.search('C:/Users/anton/Desktop/mAP-master/input/detection-results(.*)CutIn', full_name_current)
            name_current = name_current_search.group(1)[1:]
            #print("name of current file is ",name_current)
            current_file_path = Path(full_name_current)
            if current_file_path.is_file():
                components = np.loadtxt(full_name_current)
                x1c = int(components[2])
                y1c = int(components[3])
                x2c = int(components[4])
                y2c = int(components[5])
                #print("components are ",x1c,y1c,x2c,y2c)
                for otherfile in files:
                    full_name_other = os.path.join(root, otherfile)
                    name_other_search = re.search('C:/Users/anton/Desktop/mAP-master/input/detection-results(.*)CutIn', full_name_other)
                    name_other = name_other_search.group(1)[1:]
                    if name_current == name_other and full_name_current != full_name_other:
                        #print("name of other file is ",name_other)
                        other_file_path = Path(full_name_other)
                        if other_file_path.is_file():
                            components_other = np.loadtxt(full_name_other)
                            x1o = int(components_other[2])
                            y1o = int(components_other[3])
                            x2o = int(components_other[4])
                            y2o = int(components_other[5])
                            #print("components_other are ",x1o,y1o,x2o,y2o)
                            if (abs(x1c-x1o) < similarityMargin and abs(y1c-y1o) < similarityMargin and abs(x2c-x2o) < similarityMargin and abs(y2c-y2o) < similarityMargin) or (abs((x1c+y1c+x2c+y2c)-(x1o+y1o+x2o+y2o)) < 4*similarityMargin):
                                # this means the detections are too similar, must delete one
                                confc = float(components[1])
                                confo = float(components_other[1])
                                if confc > confo:
                                    os.remove(full_name_other)
                                elif confo > confc and current_file_path.is_file():
                                    os.remove(full_name_current)
                                elif confc == confo and current_file_path.is_file():
                                    sizeBoxC = (x2c - x1c)*(y2c - y1c)
                                    sizeBoxO = (x2o - x1o)*(y2o - y1o)
                                    if sizeBoxC > sizeBoxO and current_file_path.is_file():
                                        os.remove(full_name_other)
                                    elif (sizeBoxC < sizeBoxO or sizeBoxC == sizeBoxO) and current_file_path.is_file():
                                        os.remove(full_name_current)

"""
Created on Fri Nov 26 11:57:50 2021

4. Merge files with same beginning name

For each file if a file where full_name = name does not exist
    Create it
    Append the contents to the new file
If it does exist
    Append the contents to the new file
Delete all files that contain the word random
"""


import os
import re
from pathlib import Path

dir_path = 'C:/Users/anton/Desktop/mAP-master/input/detection-results'

for root, dirnames, files in os.walk(dir_path, topdown=False):
        for file in files:
            full_name_current = os.path.join(root, file)
            #print("full_name_current is ",full_name_current)
            name_current_search = re.search('C:/Users/anton/Desktop/mAP-master/input/detection-results(.*)CutIn', full_name_current)
            name_current = name_current_search.group(1)[1:]
            #print("name of current file is ",name_current)
            current_file_path = Path(full_name_current)
            full_info_file_path = dir_path + '/' + name_current + '.txt'
            #print("full_info_file_path is ",full_info_file_path)
            path = Path(full_info_file_path)
            if path.is_file():
                #print("full_info_file exists")
                textIn = open(full_name_current, "r")
                textAppend = textIn.read()
                textIn.close()
                full_info_file = open(path,"a")
                #print("opened the existing file")
                full_info_file.write(textAppend)
                full_info_file.close()
            else:
                #print("full_info_file does not exist yet")
                textIn = open(full_name_current, "r")
                textAppend = textIn.read()
                textIn.close()
                full_info_file = open(path,"a+")
                #print("created file")
                full_info_file.write(textAppend)
                full_info_file.close()
            if "random" in full_name_current:
                os.remove(full_name_current)
