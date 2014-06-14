#!/bin/bash

for i in 400000 500000 600000 700000 800000 900000 1000000
do
	echo userspace > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
	echo $i > /sys/devices/system/cpu/cpu0/cpufreq/scaling_setspeed
	echo Frequency : $i
        sudo cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq
#cd ~/ELEC-FaceCloud/USBCAMERA-app/

# Run program in background 
#sudo rm -r 2013-12-06
./run.py > ~/usbcam.log >& ~/usbcam.err
done


