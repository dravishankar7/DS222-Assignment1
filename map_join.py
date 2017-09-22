#!/usr/bin/env python
import sys

for line in sys.stdin:
        line = line.strip()
        key, value = line.split('\t')
        key= key.strip()
        value = value.strip()
        print('{0}\t{1}'.format(key,value)) 
