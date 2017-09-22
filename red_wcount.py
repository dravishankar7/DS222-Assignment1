#!/usr/bin/env python
import sys

c_word = None
c_label = None
cw_count = 0
word = None
label = None
wl_dict = {}

for line in sys.stdin:
        line = line.strip()
        word, label = line.split('\t')
        #lab, count = with_label.split()
        #count = int(count)
        
        if c_word == word:
		if c_label == label:
			if c_label in wl_dict:
                                wl_dict[c_label] += 1
                        else:
                                wl_dict[c_label] = 1
		else:
			if c_label in wl_dict:
				wl_dict[c_label] += 1
			else:
				wl_dict[c_label] = 1
			c_label = label 
                
        else:
		if c_word:
			if c_label in wl_dict:
                               	wl_dict[c_label] += 1
                       	else:
                               	wl_dict[c_label] = 1
                
			print('{0}\t{1}'.format(c_word,wl_dict))
			wl_dict.clear()
		
		c_word = word
		c_label = label
				       

if c_word == word:
	if c_label in wl_dict:
		wl_dict[c_label] += 1
        else:
		wl_dict[c_label] = 1

	print('{0}\t{1}'.format(c_word,wl_dict))





