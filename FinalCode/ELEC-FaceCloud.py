#!/usr/bin/python

import sys
import os
import cv2.cv as cv
import cv2
from optparse import OptionParser
import numpy as np 
import RPi.GPIO as GPIO
import time
import smtplib
import FolderActions as f 
import IO
from common import clock

min_size = (20, 20)
image_scale = 2
haar_scale = 1.2
min_neighbors = 2
haar_flags = 0

noface = 0
current_time = 0
dailyfolder = 0 

capture = 0 
cascade = 0

#size of video 
width = 160 
height = 120

frame_copy = 0 	



def detect_and_draw(img, cascade):
    # allocate temporary images
    gray = cv.CreateImage((img.width,img.height), 8, 1)
    small_img = cv.CreateImage((cv.Round(img.width / image_scale),
			       cv.Round (img.height / image_scale)), 8, 1)
    
    global noface
    global current_time
    global dailyfolder
    global imagenum
    global t1 

    current_time=time.strftime("%H:%M:%S")
    dailyfolder=time.strftime("%F")
    FileName="/Detected-Faces/"
    FileName=dailyfolder+FileName+current_time+ ".jpeg"
    cropFileName = "/FaceCapture/"
    cropFileName=dailyfolder+cropFileName
    # convert color input image to grayscale
    cv.CvtColor(img, gray, cv.CV_BGR2GRAY)

    # scale input image for faster processing
    cv.Resize(gray, small_img, cv.CV_INTER_LINEAR)
    cv.EqualizeHist(small_img, small_img)

    if(cascade):
        t = clock()
        faces = cv.HaarDetectObjects(small_img, cascade, cv.CreateMemStorage(0),
                                     haar_scale, min_neighbors, haar_flags, min_size)
        t = clock() -t 
       
        if faces:
	    imagenum = imagenum +1
	    print ("face")
	    i = 0
            for ((x, y, w, h), n) in faces:
		i = i +1
                cropFileName = cropFileName + "face"+ str(imagenum)+ "_" + str(i) + ".jpeg"
		#cropFilename =cropFilename + 'face.jpeg'
                # the input to cv.HaarDetectObjects was resized, so scale the
                # bounding box of each face and convert it to two CvPoints
                pt1 = (int(x * image_scale), int(y * image_scale))
                pt2 = (int((x + w) * image_scale), int((y + h) * image_scale))
                cv.Rectangle(img, pt1, pt2, cv.RGB(255, 0, 0), 3, 8, 0)
	        cropimg = img[int(y*image_scale):int((y+h)*image_scale), int(x*image_scale):int((x+w)*image_scale)]
		cv.SaveImage(cropFileName,cropimg)
		#cv.SaveImage(cropFileName,img)
		#### DEBUG ### 
		#IO.LEDON()
		#time.sleep(1)
		#IO.LEDOFF()
                
	    #imagenum = imagenum+1
	    # save image ; update log 
	    cv.SaveImage(FileName,img)
	    f.updatelog(imagenum,i,t,t1)

	    del(gray)
	    del(small_img)

	else:
		del(gray)
		del(small_img)


def USBCameraSetup(): 

    global capture
    global cascade
    global width
    global height 
    global frame_copy

    cascade = cv.Load('face.xml')
    capture = cv.CreateCameraCapture(0)

    if not capture :
    	print "Error loading camera"


    if width is None:
    	width = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH))
    else:
    	cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_WIDTH,width)

    if height is None:
	height = int(cv.GetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT))
    else:
	cv.SetCaptureProperty(capture,cv.CV_CAP_PROP_FRAME_HEIGHT,height)

    if capture:
        frame_copy = None

imagenum =0
if __name__=='__main__':

        #status LED connects to gpio pin 24
        #can use status LED for debugging
        #or varification of a positive face ID

        # how to turn LED on/off
        #     IO.LEDON()
        #     IO.LEDOFF()

	

        USBCameraSetup()

        IO.SetupGPIOPins()
        a = f.makedailyfolder()
	if a == 1:
	   imagenum=0
        f.newlog()

	global noface
	global capture
	global frame_copy
	global cascade 
	global t1
	global t2
	#while True:
	for i in range(0,100):
        	frame = cv.QueryFrame(capture)
                
            	if not frame:
                	cv.WaitKey(0)
                	break
            	if not frame_copy:
                	frame_copy = cv.CreateImage((frame.width,frame.height),cv.IPL_DEPTH_8U, frame.nChannels)

		t1 = clock()
            	if frame.origin == cv.IPL_ORIGIN_TL:
                	cv.Copy(frame, frame_copy)
            	else:
                	cv.Flip(frame, frame_copy, 0)
		t1 = clock() - t1
		#IO.LEDON()
            	detect_and_draw(frame_copy, cascade)
		#IO.LEDOFF()
		


