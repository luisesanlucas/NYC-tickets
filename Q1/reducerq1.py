#!/usr/bin/python

from operator import itemgetter
import sys
from collections import defaultdict

dict_count = {}

for line in sys.stdin:
    line = line.strip()
    try:
        time, num = line.split('\t')
        num = int(num)
        dict_count[time] = dict_count.get(time,0) + num
    except ValueError:
        pass


sorted_dict_count = sorted(dict_count.items(), key=itemgetter(1),reverse=True)

print('Tickets most likely to be issued at:')
for h in sorted_dict_count[:10]:
    print(h)
 