#!/usr/bin/env python2

csv_fname = 'jobs_summary.csv'

# without lib
#with open(csv_fname, 'r') as f:
#    lines = [line.strip().split(',') for line in f]

#with lib
import csv
with open(csv_fname, 'r') as f:
    dictlist = [line for line in csv.DictReader(f)]

print dictlist

