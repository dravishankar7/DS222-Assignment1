#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 04:14:32 2017

@author: ravi
"""

import string
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import numpy as np
import math
import time
import re


start = time.time()

'''
print('SMALL DATA')
train_path = "/home/ravi/Documents/MLLDS/DBPedia.verysmall/verysmall_train.txt"
dev_path = "/home/ravi/Documents/MLLDS/DBPedia.verysmall/verysmall_devel.txt"
test_path = "/home/ravi/Documents/MLLDS/DBPedia.verysmall/verysmall_test.txt"
'''
print('FULL DATA')
train_path = "/home/ravi/Documents/MLLDS/DBPedia.full/full_train.txt"
dev_path = "/home/ravi/Documents/MLLDS/DBPedia.full/full_devel.txt"
test_path = "/home/ravi/Documents/MLLDS/DBPedia.full/full_test.txt"


#train_path = "/home/ravi/Documents/MLLDS/Assignment1/sample_train.txt"
#dev_path = "/home/ravi/Documents/MLLDS/Assignment1/sample_dev.txt"
#test_path = "/home/ravi/Documents/MLLDS/Assignment1/sample_test.txt"


    
def stopWords(sent):
    sent = re.sub(r'[^a-zA-Z]', " ", sent)
    stop = stopwords.words('english')
    stop.append('also')
    sent = sent.lower().translate(str.maketrans({key: None for key in string.punctuation}))
    sent = ' '.join([word for word in sent.split() if word not in stop if not word.isdigit() if len(word)>3])
    return sent
    
def readData(file):
    arr_labels = []
    arr_sent = []
    for line in file:
        labels, sent = line.split("\t",1)
        labels = labels.strip()
        sent = sent.strip()
        arr_labels.append(labels.split(","))
        soup = BeautifulSoup(sent, 'html.parser')
        sent = soup.get_text()
        arr_sent.append(stopWords(sent))
    return arr_labels, arr_sent
        

with open(train_path) as text_train:
    train_file = text_train.readlines()
with open(dev_path) as text_dev:
    dev_file = text_dev.readlines()
with open(test_path) as text_test:
    test_file = text_test.readlines()

'''
train_lab_text, train_sent = readData(train_file[3:len(train_file)])
dev_lab_text, dev_sent = readData(dev_file[3:len(dev_file)])
test_lab_text, test_sent = readData(test_file[3:len(test_file)])
'''

train_lab_text, train_sent = readData(train_file)
dev_lab_text, dev_sent = readData(dev_file)
test_lab_text, test_sent = readData(test_file)


end1 = time.time()
print("time to preprocess data ", end1 - start)

def labDict(labels):
    lab_dict = {}
    for i in range(len(labels)):
        for k in range(len(labels[i])):
            if labels[i][k] not in lab_dict:
                lab_dict[labels[i][k]] = len(lab_dict)
    return lab_dict

lab_dict = labDict(train_lab_text)

def labNum(labels_text):
    lab_list = []
    for i in range(len(labels_text)):
        vec = []
        for j in range(len(labels_text[i])):
            vec.append(lab_dict[labels_text[i][j]])
        lab_list.append(vec)
    return lab_list

train_lab_num = labNum(train_lab_text)
dev_lab_num = labNum(dev_lab_text)
test_lab_num = labNum(test_lab_text)       

lab_count = {}
for i in range(len(train_lab_num)):
    for j in range(len(train_lab_num[i])):
        if train_lab_num[i][j] in lab_count:
            lab_count[train_lab_num[i][j]] += 1
        else:
            lab_count[train_lab_num[i][j]] = 1

lab_prob = np.zeros(shape = [len(lab_dict)])
for key in lab_count:
    lab_prob[key] = math.log(lab_count[key] / len(train_sent))

s_w = time.time()

w_dict = {}
for i in range(len(train_sent)):
    for word in train_sent[i].split():
        if word not in w_dict:
            w_dict[word] = len(w_dict)
            

e_w = time.time()
#print("time to create word dictonary: ", e_w - s_w)
    
#creating matrix of words with the counts
#word_mat = np.ones(shape = [len(w_dict), len(lab_dict)])
word_mat = np.zeros(shape = [len(w_dict), len(lab_dict)])
for i in range(len(train_sent)):
    for word in train_sent[i].split():
        if word in w_dict:
            index = w_dict[word]
            for j in range(len(train_lab_num[i])):
                word_mat[index][train_lab_num[i][j]] += 1
                

e_wm = time.time()
#print("time to create word matrix: ", e_wm - e_w)
    

#totalling no.of words for each label
lab_sum = np.zeros(shape = [len(lab_dict)])
for i in range(len(lab_dict)):
    for j in range(len(w_dict)):
        lab_sum[i] += word_mat[j][i] 
        

# proba = dividing each value with the total and then taking log 
smoothing = 1        
#smoothing = 1/max(lab_count.values())
for i in range(len(w_dict)):
    for j in range(len(lab_dict)):
        if word_mat[i][j] == 0:
            word_mat[i][j] = math.log(1*smoothing/ (1+lab_sum[j]))
        else:
            word_mat[i][j] = math.log(word_mat[i][j] / lab_sum[j])
            

            
'''''''''''''''''''''''''''''''''prediction'''''''''''''''''''''''''''''
print("time for training: ",s_train-start)
print("Inference")
#print("with label prob")
s_train = time.time()
#trining set
train_pred = np.zeros(shape = [len(train_sent), 2])
for i in range(len(train_sent)):
    sent_sum = np.zeros(shape = [len(lab_dict)])
    for word in train_sent[i].split():
        if word in w_dict:
            index = w_dict[word]
            for j in range(len(lab_dict)):
                sent_sum[j] += word_mat[index][j]
#    for k in range(len(lab_dict)):
#        sent_sum[k] += lab_count[k]
    pred_lab_index = np.where(sent_sum == max(sent_sum))
    f_class = pred_lab_index[0][0]
    if f_class in train_lab_num[i]:
        train_pred[i][0] = 1;
        train_pred[i][1] = f_class;
              
train_correct = 0
for i in range(len(train_sent)):
    train_correct += train_pred[i][0]
train_acc = (train_correct * 100)/len(train_sent)
    
e_train = time.time()

#development set
dev_pred = np.zeros(shape = [len(dev_sent), 2])
for i in range(len(dev_sent)):
    sent_sum = np.zeros(shape = [len(lab_dict)])
    for word in dev_sent[i].split():
        if word in w_dict:
            index = w_dict[word]
            for j in range(len(lab_dict)):
                sent_sum[j] += word_mat[index][j]
#    for k in range(len(lab_dict)):
#        sent_sum[k] += lab_count[k]
    lab_index = np.where(sent_sum == max(sent_sum))
    f_class = lab_index[0][0]
    if f_class in dev_lab_num[i]:
        dev_pred[i][0] = 1;
        dev_pred[i][1] = f_class;
'''
    print("f_class: ", f_class)
    print("dev_lab_num : ", dev_lab_num[i])
'''   
     
dev_correct = 0
for i in range(len(dev_sent)):
    dev_correct += dev_pred[i][0]
dev_acc = (dev_correct * 100)/len(dev_sent)


e_dev = time.time()

#test set
test_pred = np.zeros(shape = [len(test_sent), 2])
for i in range(len(test_sent)):
    sent_sum = np.zeros(shape = [len(lab_dict)])
    for word in test_sent[i].split():
        if word in w_dict:
            index = w_dict[word]
            for j in range(len(lab_dict)):
                sent_sum[j] += word_mat[index][j] 
#    for k in range(len(lab_dict)):
#        sent_sum[k] += lab_count[k]
    lab_index = np.where(sent_sum == max(sent_sum))
    f_class = lab_index[0][0]
    test_pred[i][1] = f_class;
    if f_class in test_lab_num[i]:
        test_pred[i][0] = 1;
    else:
        test_pred[i][0] = 0;

test_correct = 0
for i in range(len(test_sent)):
    test_correct += test_pred[i][0]
test_acc = (test_correct * 100)/len(test_sent)

e_test = time.time()



print("training accuracy: ", train_acc)
print("development accuracy: ", dev_acc)
print("test set accuracy: ", test_acc)   

print("time to test training set: ", e_train - s_train)
print("time to test dev set: ", e_dev-e_train)
print("time to test test set: ", e_test-e_dev)    
print('Total time: ', e_test-start)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    