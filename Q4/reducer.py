#!/usr/bin/python
from operator import itemgetter
import sys

dict_count = {}

for line in sys.stdin:
    line = line.strip()
   
    try:
        color, num = line.split('\t')
        num = int(num)	
        dict_count[color] = dict_count.get(color, 0) + num
    except ValueError:
        pass


print('this color of the vehicle is the most likely to get a ticket')
sorted_dict_count = sorted(dict_count.items(), key=itemgetter(1),reverse=True)

top_n = sorted(sorted_dict_count, key=lambda v:v[1], reverse=True)[0:3]
print '%s' % (top_n)
