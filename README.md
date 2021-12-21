# AC-Object-Detection-in-Panoramas
MEng Thesis. Detecting AC components using YOLOv4: Comparison of panoramic image processing pipelines.

# Dataset processing
Dataset management

  * PNGtoJPG.py - Converts PNG files to JPG files, the format of the majority
  
  * resizeImage.py - Adapted from Reine (2021), resizes images to the desired number of pixels to avoid excessively long loading times
  
  * changeFileName.py - Changes the file name as required

Processing pipelines

  * panoToCubes.py - Converts panoramic images to cube faces
  
  * panoToStereos.py - Adapted from Yang (2018), converts panoramic images to stereographic projections
  
  * panoToTiles.py - Adapted from Kufuor (2020), subdivides panoramic images into eight tiles

# Model training
Adapted from The AI Guy (2020) - see source for folder/file structure:

  * YOLOv4_Training_Tutorial.ipynb - Trains the model according to the parameters set in the configuration file, the image paths and object classes in the files below
  
  * generate_train.py, generate_valid.py, and generate_test.py - Loop through the images and create one file with all the training image paths, another for validation image paths and another for testing
  
  * object.names and object.data - State the class names and the paths to training, validation and testing images for the model to read
  
  * yolov4-obj.cfg - Configuration file, states the parameters

# Model testing

  * ModelOnPython.py - Adapted from cyberdong (2021), allows to use the model locally
  
Adapted from Cartucho (2018) - see source for folder/file structure: 
  
  * convert_dr_yolo.py - Converts the result files (detections) outputted by the model into files in a format compatible for comparison with the ground truths
  
  * convert_gt_yolo.py - Converts the ground truth labels into a compatible format for comparison. YOLO labels define bounding box coordinates through its central coordinates, width, and height. This script translates those into the coordinates of the top left and bottom right corners
  
  * main.py - Compares the detections and ground truths, then calculates mAP and all intermediary necessary steps (true positives, false positives and false negatives, the precision-recall curve)
  
  * convert_dr_yolo_LocalToGlobalCoords.py - Equivalent to the convert_dr_yolo.py, but used when detections were performed on tiled panoramas to convert detections to the global panorama coordinate system, performing the relevant bounding box selection
