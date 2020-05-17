#!/usr/bin/python

import sys

hits = 0
oldKey = None
maxHits = 0
maxKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) == 2:
	thisKey, thisCount = data_mapped

   	if oldKey and oldKey != thisKey:
            if maxHits < hits:
            	maxHits = hits
		maxKey = oldKey
	    oldKey = thisKey
            hits = 0

        oldKey = thisKey
        hits += float(thisCount)

print maxKey, "\t", maxHits

