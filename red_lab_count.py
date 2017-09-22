#! /usr/bin/env python
import sys



c_label = None
c_noofword = 0
c_count = 0
label = None    
for line in sys.stdin:
        line = line.strip()
        label,noofword = line.split()
        noofword = int(noofword)
        if c_label == label :
                c_noofword += noofword
                c_count += 1
        else:
                if c_label:
                        print('{0}\t{1}\t{2}'.format(c_label, c_noofword, c_count))
                
                c_label = label
                c_noofword = noofword
                c_count = 1

if c_label == label:
        print('{0}\t{1}\t{2}'.format(c_label, c_noofword, c_count))



