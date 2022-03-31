# -*- coding: utf-8 -*-
"""
Adapted from
https://github.com/cyberdong/yolo_opencv-python_cpu
"""

import numpy as np
import cv2 as cv
import os
import time
import glob

# CHANGE THESE TO YOURS - this is the only part that absolutely requires modification
weightsPath = 'C:/Users/anton/Desktop/BoanModel/Boan+Cubes/yolov4-obj_last.weights'
configPath = 'C:/Users/anton/Desktop/BoanModel/yolov4-obj.cfg'
labelsPath = 'C:/Users/anton/Desktop/BoanModel/obj.names'
#test_img = 'C:/Users/anton/Desktop/Datasets/PanosTiled/test/Relevant ConcealedVents0_37848707.jpg'
images_path = 'C:/Users/anton/Desktop/Datasets/PanoSliding/On PanoSlidesTest/PanoSlidesTest/AllTiled'
results_path = 'C:/Users/anton/Desktop/mAP-master/scripts/extra'

CONFIDENCE = 0
THRESHOLD = 0.4  # NMS

net = cv.dnn.readNetFromDarknet(configPath, weightsPath)
print("[INFO] loading YOLO from disk...")

# Create a text file called result to store detections
file = 'resultTrying.txt'
with open(os.path.join(results_path, file), 'a+') as detections_text_file:
    for test_img in glob.glob(images_path + '/*.jpg'):
        print("now I'm going to a new image")
        # Load the picture, convert it to blob format, and send it to the network input layer
        img = cv.imread(test_img)
        blobImg = cv.dnn.blobFromImage(img, 1.0/255.0, (416, 416), None, True, False)
        net.setInput(blobImg)
        
        # Get network output layer information (names of all output layers), set and forward it
        outInfo = net.getUnconnectedOutLayersNames()
        start = time.time()
        layerOutputs = net.forward(outInfo)
        end = time.time()
        print("[INFO] YOLO took {:.6f} seconds".format(end - start))
        
        (H, W) = img.shape[:2]
        boxes = []
        confidences = []
        classIDs = []
        
        print("We're now starting the for loop") 
        # # 1) Filter out frames with low confidence
        for out in layerOutputs:
            for detection in out:
                # Get the confidence
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]
        
                # Screening based on confidence
                # print("loop") 
                if confidence > CONFIDENCE:
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)
        
        # print("Finished the for loop!") 
        
        # # 2) Apply non-maxima suppression (nms)
        idxs = cv.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, THRESHOLD)
        with open(labelsPath, 'rt') as f:
            labels = f.read().rstrip('\n').split('\n')
        np.random.seed(42)
        COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")
        if len(idxs) > 0:
            for i in idxs.flatten():
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])
                
        # # 3) Append detection results to text file
        # Append a line that refers to the image
        detections_text_file.write("\n" + test_img + ": Predicted in {:.6f} seconds".format(end - start) + ".")
        # Append one line for each detection in that image, including class name, confidence, and coordinates
        if len(idxs) > 0:
            for i in idxs.flatten():
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])
                detections_text_file.write("\n" + labels[classIDs[i]] + ": " + str(int(confidences[i]*100)) + "% (left_x: " + str(x) + " top_y: " + str(y) + " width: " + str(w) + " height: " + str(h) + ")")
        """
        wall_mounted_indoor_hvac: 98%	(left_x:    4   top_y:  138   width:  183   height:  202)
        cassettes_indoor_hvac: 27%	(left_x:    4   top_y:  139   width:  180 
        """
        """
                color = [int(c) for c in COLORS[classIDs[i]]]
                cv.rectangle(img, (x, y), (x+w, y+h), color, 2)
                text = "{}: {:.4f}".format(labels[classIDs[i]], confidences[i])
                cv.putText(img, text, (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        cv.imshow('detected image', img)
        cv.waitKey(0)
        print("printed image")
        """
