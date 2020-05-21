#!/usr/bin/python

import csv
from datetime import datetime

import sys


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

next(reader)
for line in reader:
    student_id, timestamp = line[3], line[8]
    timestamp = timestamp.replace('+00', '')
    hour = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f").hour
    print "{0}\t{1}".format(student_id, hour)

