# Harmful Object Detection 

###### Required libraries 
 * OpenCV (***pip install opencv-python***)
 * Numpy (***pip install numpy***)
 
To download Cascade Trainer, visit https://amin-ahmadi.com/cascade-trainer-gui/

Cascade Trainer GUI is a program that can be used to train, test and improve cascade classifier models. It uses a graphical interface to set the parameters and make it easy to use OpenCV tools for training and testing classifiers.
- If you are new to the concept of object detection and classifiers please consider visiting http://opencv.org for more information.
  
## 1)  Why this concept?
   - Anyone who is new with computer vision applications and wanted to go with the first project, this is the great and interesting experiment that you can try.
## 2)  How this algorithm works?
   - It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images. If you want to go deeper in this Please check this link http://www.willberger.org/cascade-haar-explained/  .
   - A Haar-Feature is just like a kernel in CNN, except that in a CNN, the values of the kernel are determined by training, while a Haar-Feature is manually determined.
   - Here are some Haar-Features. The first two are “edge features”, used to detect edges. The third is a “line feature”, while the fourth is a “four rectangle feature”, most likely used to detected a slanted line.

## 3)  Advantages
   - 1) Significantly faster than other heavy models
   - 2) Easy to train and also easy to implement using Python
   - 3) Can be used on Edge devices like Raspberry Pi and Jetson.
## 4)  Disadvantages
   - 1) This is not like a professional models availble on internet or in market that we can use
   - 2) Lacks in accuracy when it comes to the noicy input and small objects
## 5) What Are the Basic Assumption
   - Moving object detection under a moving camera has long been a very challenging task as the movements of the moving objects and motion caused by the camera are merged in the image sequence.
## 6) In which problem statement you can your this concept or Algorithm?
   - You can use this as your hello world of object detection if you wanted to perform it on Edge devices. Also you can use it where you want to detect the a single object, you can use this technique.
    
  
    
