#!/usr/bin/env python

import sys
import string
import csv

for line in sys.stdin:
    try:
	columns = line.split(',')
        colors = columns[33]
    except IndexError:
        pass


    print '%s\t%s' % (colors,1)



