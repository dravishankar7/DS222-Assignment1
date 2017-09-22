#!/usr/bin/env python
import sys

for line in sys.stdin:
        line = line.strip()
        divide = line.split()
        labels = divide[0]
        sent = divide[1:]
        for l in labels.split(","):
                value = str(len(sent))
                print('{0}\t{1}'.format(l,value))









