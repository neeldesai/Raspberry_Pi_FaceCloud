#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from array import *

#print data
x=array('i',[0])
y=array('d',[0.0])
freq=400
temp_x=0
for p in range(0,5,1):
	with open("/home/jay/Dropbox/ELEC-FaceCloud/OneFace_Scale3/2013-12-13/logFaces_" + str(freq)  + ".txt") as f:
		data = f.read()
	data = data.split('\n')
	for i in range(0,70,1):
		temp=data[i]
		temp1= temp.split(',')
		print temp1[3]
	        temp2=float(temp1[3])
	        y.append(temp2)
        	x.append(temp_x)
                temp_x=temp_x + 1
	freq=freq+100
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title("Rpi Facecloud")    
ax1.set_xlabel('Sample number')
ax1.set_ylabel('execution time')
ax1.plot(x,y, c='r')
leg = ax1.legend()
plt.show()
