#! /usr/bin/env python
import sys
import ast


c_word = None
word = None
linenum  = []        
w_dict = {}

for line in sys.stdin:
        line = line.strip()
        word, value = line.split('\t')
        if c_word == word:
                if value[0] == '{':
                        w_dict = ast.literal_eval(value)
                else:
                     linenum.append(value)
        
        else:             
                if c_word:
                        if (len(linenum) > 0 and len(w_dict) > 0):
                                for i in range(len(linenum)):
                                        print('{0}\t{1}'.format(linenum[i], w_dict))
                                w_dict = {}
                                        
                del linenum[:]
                c_word = word
                if value[0] == '{':
                        w_dict = ast.literal_eval(value)
                else:
                        linenum.append(value)
                        
if c_word == word:
        if(len(linenum) > 0 and len(w_dict) > 0):
                for i in range(len(linenum)):
                        print('{0}\t{1}'.format(linenum[i], w_dict))

