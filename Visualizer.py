import cv2
import cv2.cv as cv
import numpy as np


if __name__ == '__main__':

    ##########################################
    # Openning and configuring Kinect Camera #
    ##########################################
    capture = cv2.VideoCapture(cv.CV_CAP_OPENNI)
    if not capture.isOpened():
        print "Cannot open kinect sensor"
        exit()
    
    capture.set(cv.CV_CAP_OPENNI_IMAGE_GENERATOR_OUTPUT_MODE, cv.CV_CAP_OPENNI_VGA_30HZ)
    capture.set(cv.CV_CAP_PROP_OPENNI_REGISTRATION,1)
    
    while True:
        capture.grab()
        okImaBGR , imaBGR = capture.retrieve(0,cv.CV_CAP_OPENNI_BGR_IMAGE)
        okImaXYZ , imaXYZ = capture.retrieve(0,cv.CV_CAP_OPENNI_POINT_CLOUD_MAP)
        
        cv2.imshow("imaBGR", imaBGR)    
        cv2.imshow("imaXYZ", imaXYZ)    
        cv2.waitKey(10)
    capture.release()
    exit()