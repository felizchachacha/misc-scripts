#!/usr/bin/env python2.7

import re
from datetime import datetime, timedelta

#settings
source_dir = "logs/"
datetime_format = '%d/%b/%Y:%H:%M:%S'
log_file_name_format = "%Y_%m_%d_%H"
minutes_to_print = 10

#apache combined log format
parts = [
    r'(?P<host>\S+)',  # host %h
    r'\S+',  # indent %l (unused)
    r'(?P<user>\S+)',  # user %u
    r'\[(?P<time>.+)\]',  # time %t
    r'"(?P<request>.*)"',  # request "%r"
    r'(?P<status>[0-9]+)',  # status %>s
    r'(?P<size>\S+)',  # size %b (careful, can be '-')
    r'"(?P<referrer>.*)"',  # referrer "%{Referer}i"
    r'"(?P<agent>.*)"',  # user agent "%{User-agent}i"
]

Pattern = re.compile(r'\s+'.join(parts) + r'\s*\Z')

#function to print selected amount of minutes from now from the logfile of selected date
def printlogs(now, selected_date, minutes):
    file_name = source_dir + datetime.strftime(selected_date, log_file_name_format) + ".log"
    try:
        file = open(file_name)
    except IOError as e:
        print 'Error opening file'
    else:
        with file as f:
            for line in f:
                Fields = Pattern.match(line).groupdict() #extracting fields
                if Fields["status"] == "500":
                    line_datetime = Fields["time"][0:20] #extracting datetime
                    time_delta = (now - datetime.strptime(line_datetime, datetime_format)).total_seconds() #calculating time difference
                    if 0 < ( time_delta / 60 ) <= minutes:
                        print line


now = datetime.now()
cur_minute = now.minute

if int(cur_minute) < minutes_to_print:      #if current minute < minutes to print then we should print from 2 different logfiles:
    prev_hour = now - timedelta(hours=1)
    printlogs(now, prev_hour, minutes_to_print - cur_minute)    #print from logfile of previous hour
    printlogs(now, now, cur_minute)                             #print from latest logfile
else:
    printlogs(now, now, minutes_to_print)   #otherwise we are printing only from the latest logfile
