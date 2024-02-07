#!/usr/bin/env python

import sys

result = {}

for line in sys.stdin:
    key, value = line.strip().split(' ')
    if result.get(key) == None:
        sum = int(value)
    else:
        sum += int(value)
    result.update({key:sum})

for key,value in result.items():
    print(f'{key}\t{value}')