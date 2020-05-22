#/usr/bin/python

import sys

question_id = None
student_id_list = []

for line in sys.stdin:
    this_question_id, student_id = line.strip().split('\t')
    
    if question_id is not None and question_id != this_question_id:
        print "{0}\t{1}".format(question_id, student_id_list)
	student_id_list = []

    question_id = this_question_id
    student_id_list.append(student_id)

if question_id is not None:
    print "{0}\t{1}".format(question_id, student_id_list)
    
