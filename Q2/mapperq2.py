#!/usr/bin/python
# --*-- coding:utf-8 --*--
import re
import sys

for line in sys.stdin:
    columns = line.split(',')
    vtype=columns[6].strip()
    #year=0
    year=columns[35].strip()
   
    try:
        year=int(year)
        if year==0:
            next
        else:
            print ('%s\t%s' % (str(year)+ ' ' + vtype, 1))
    except ValueError, TypeError:
        next