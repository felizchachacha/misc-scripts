#!/usr/bin/env python2.7

import glob
import os

#settings
logs_dir="logs/"
target='vagrant@192.168.33.10:/tmp/'


os.chdir(logs_dir)
fileList = glob.glob("*_*_*_*.log")

for item in fileList:
	print item
	hour = int(item[len(item)-6:len(item)-4]) #extracting hour from the file name
	if 18 <= hour <= 21:
		print hour
		os.system("scp " + item + " " + target)
