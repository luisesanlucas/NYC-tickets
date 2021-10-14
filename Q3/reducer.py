#!/usr/bin/python
from operator import itemgetter
import sys

dict_count = {}

for line in sys.stdin:
    line = line.strip()
    
    try:
	location, num = line.split('\t')
        num = int(num)
        dict_count[location] = dict_count.get(location, 0) + num

    except ValueError:
        pass
    
sorted_dict_count = sorted(dict_count.items(), key=itemgetter(1), reverse=True)
#for location, count in sorted_dict_count:
#    print '%s\t%s' % (location, count) 
print('These places are tickets most commonly issued')
top_n = sorted(sorted_dict_count, key=lambda v:v[1], reverse=True)[0:3]
print '%s' % (top_n)           
