#!/bin/python

import os 
import time
import subprocess
import sys

def run_command(command):
    p=subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)
    return p.communicate()



def makedailyfolder(): 
	
	DailyFolder=time.strftime("%F")
	DailySubFolder=DailyFolder+"/"+"Detected-Faces"
        DailySubFolder2 =DailyFolder+"/"+"FaceCapture" 
        if (not os.path.exists(DailyFolder)):
	   os.mkdir(DailyFolder)   	
        if (not os.path.exists(DailySubFolder)):
	   os.mkdir(DailySubFolder)
        if (not os.path.exists(DailySubFolder2)):
	   os.mkdir(DailySubFolder2)
	   return 1
	else:
	   return 0

def newlog():


        DailyFolder1=time.strftime("%F")

	x=run_command("cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq")
        freq= x[0]
        freq=freq[:3]         
        name='/logFaces'+'_'+ freq+'.txt'
	name=DailyFolder1+name
	faces = open(name, "w+b+a")
	faces.write("0,0,0,0\n")
	faces.close()

def updatelog(imagenum,numfaces,timetaken,timetaken2):

        DailyFolder1=time.strftime("%F")
        x=run_command("cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq")
        freq= x[0]
        freq=freq[:3]
        name='/logFaces'+'_'+ freq+'.txt'
        #name="/logFaces.txt"
        name=DailyFolder1+name
	ourlog = file(name, "a+r")
	data=ourlog.read(2)
	
	timestamp=time.strftime("%H:%M:%S")
	outputstring=str(imagenum)+","+timestamp + "," + str(numfaces)+"," + str(timetaken)+","+ str(timetaken2) + "\n"
	
	ourlog.write(outputstring)

        ourlog.close()






