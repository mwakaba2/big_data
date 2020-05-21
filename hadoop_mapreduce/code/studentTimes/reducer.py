#!/usr/bin/python

import sys

postCount = 0
maxPostCount = 0
maxHours = []
studentId = None
hour = None

for line in sys.stdin:
    thisStudentId, thisHour = line.strip().split('\t')
    diffHour = hour is not None and thisHour != hour
    diffStudent = studentId is not None and studentId != thisStudentId
    
    if diffHour or diffStudent:
        if postCount == maxPostCount:
            maxHours.append(hour)
        elif postCount > maxPostCount:
            maxPostCount = postCount
            maxHours = [hour]
        postCount = 0
        if diffStudent:
            for hour in maxHours:
                print "{0}\t{1}".format(studentId, hour)        
            maxHours = []
            maxPostCount = 0
    
    hour = thisHour
    studentId = thisStudentId    
    postCount += 1

if studentId is not None:
    if postCount == maxPostCount:
        maxHours.append(hour)
    elif postCount > maxPostCount:
        maxHours = [hour]

    for hour in maxHours:
        print "{0}\t{1}".format(studentId, hour)

