#!/usr/bin/python

import csv
import sys


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    tags, node_type = line[2].strip().split(' '), line[5]

    if node_type == 'question':
	for tag in tags:
	    writer.writerow([tag])

