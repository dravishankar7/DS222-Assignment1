#! /usr/bin/env python
import sys

for line in sys.stdin:
	labels, sent = line.split('\t')
	#lineno = str(lineno)
        for word in sent.split():
		for l in labels.split(","):
			#lkey = l+'~'+lineno
                   	print('{0}\t{1}'.format(word,l))




