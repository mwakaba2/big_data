#!/usr/bin/python

import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

next(reader)
for line in reader:
    node_id, author_id, node_type, abs_parent_id = line[0], line[3], line[5], line[7]
    
    if node_type == 'question':
	post_id = node_id
    else:
	post_id = abs_parent_id

    writer.writerow([post_id, author_id])

