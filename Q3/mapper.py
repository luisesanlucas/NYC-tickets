#!/usr/bin/env python

import sys
import string
import csv

for line in sys.stdin:
    try:
        columns=line.split(',')
        location = columns[13]
	
    except IndexError:
	pass

    print  '%s\t%s' % (location,1)
