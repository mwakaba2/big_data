#!/usr/bin/python

import sys

tag = None
count = 0

for line in sys.stdin:
    thisTag = line.strip()

    if tag is not None and tag != thisTag:
	print "{0}\t{1}".format(count, tag)
	count = 0

    tag = thisTag
    count += 1

if tag is not None:
    print "{0}\t{1}".format(count, tag)

