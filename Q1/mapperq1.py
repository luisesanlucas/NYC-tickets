#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

for line in sys.stdin:
    columns = line.split(',')
    hour=columns[19].strip()
    try:
        hour=hour[:2]+hour[-1]
    except (IndexError, ValueError):
        pass
    print ('%s\t%s' % (hour, 1))