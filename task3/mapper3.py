#!/usr/bin/env python

import sys

for line in sys.stdin:
    input = line.strip().split('\t')[1].split(',')
    for value in input:
        print(value, 1)

    