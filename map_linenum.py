#!/usr/bin/env python
import sys


for line in sys.stdin:
	line = line.strip()
	divide = line.split()
	lineno = divide[0]
	labels = divide[1]
	sent = divide[2:]
	for word in sent:
		value = lineno+'~'+labels
		print('{0}\t{1}'.format(word,value))



