#!/usr/bin/env python
import sys


for line in sys.stdin:
    line = line.strip()
    word, value = line.split()
    print('{0}\t{1}'.format(word,value))












