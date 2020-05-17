#!/usr/bin/python


import sys
import re

log_regex = re.compile("^([\d+\.]+)\s([\w\-]+)\s([\w\-]+)\s(\[.*\])\s(\".*\")\s(\d{3})\s([\d-]+)$")
for line in sys.stdin:
    data = log_regex.search(line.strip())
    if data:
        groups = data.groups()
	if len(groups) == 7:
	    ip_addr, identity, username, timestamp, request, status_code, obj_size = groups
	    print "{0}\t{1}".format(ip_addr, 1)

