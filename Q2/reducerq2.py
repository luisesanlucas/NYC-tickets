#!/usr/bin/python

from operator import itemgetter
import sys
from collections import defaultdict

dict_count = {}

for line in sys.stdin:
    line = line.strip()
    try:
        car, num = line.split('\t')
        num = int(num)
        dict_count[car] = dict_count.get(car,0) + num
    except ValueError:
        pass


sorted_dict_count = sorted(dict_count.items(), key=itemgetter(1),reverse=True)

print('Most common car types to be ticketed:')
c=0
for h in sorted_dict_count:
    print(h)
    c+=1
    if c==10:
        break