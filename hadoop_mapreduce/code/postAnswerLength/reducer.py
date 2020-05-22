#!/usr/bin/python

import sys


postId = None
answerCount = 0.0
answerLength = 0
postLength = 0

for line in sys.stdin:
    thisPostId, thisNodeType, thisBodyLength = line.strip().split('\t')
    
    if postId is not None and postId != thisPostId:
        avgAnswerLength = answerLength / answerCount if answerCount > 0 else 0.0
        print "{0}\t{1}\t{2}".format(postId, postLength, avgAnswerLength)
	answerCount = 0.0
        answerLength = 0

    if thisNodeType == 'question':
        postLength = int(thisBodyLength)
    elif thisNodeType == 'answer':
        answerCount += 1
        answerLength += int(thisBodyLength)
    postId = thisPostId

if postId is not None:
    avgAnswerLength = answerLength / answerCount if answerCount > 0 else 0.0
    print "{0}\t{1}\t{2}".format(postId, postLength, avgAnswerLength)

