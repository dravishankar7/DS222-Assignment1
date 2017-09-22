#!/usr/bin/env python
import sys
import ast
import math

lab_prob_red = {'American_comedy_films': -4.300411260395528,
 'American_drama_films': -4.104803866889924,
 'American_film_actresses': -3.5091830821130765,
 'American_film_directors': -4.165851590045439,
 'American_films': -2.602545507780045,
 'American_male_film_actors': -3.193715589635896,
 'American_male_television_actors': -3.3757877161499894,
 'American_military_personnel_of_World_War_II': -3.7589885785643524,
 'American_people_of_Irish_descent': -4.025151707942304,
 'American_television_actresses': -3.6731752847851262,
 'Arctiidae': -5.911908905792639,
 'Articles_containing_video_clips': -3.699902933690941,
 'Association_football_defenders': -3.162679385702015,
 'Association_football_forwards': -3.1708472015295763,
 'Association_football_goalkeepers': -3.753019599441446,
 'Association_football_midfielders': -2.997673718887331,
 'Asteroids_named_for_people': -3.6796061751154165,
 'Australian_rules_footballers_from_Victoria_(Australia)': -4.317706745135959,
 'Black-and-white_films': -2.820554098847526,
 'Brazilian_footballers': -4.098618859824177,
 'British_films': -3.7613861821105066,
 'Columbia_University_alumni': -4.067439620145056,
 'Deaths_from_myocardial_infarction': -3.9412702239616024,
 'English-language_albums': -3.490548524265317,
 'English-language_films': -2.249228782992292,
 'English-language_journals': -4.3474539810406885,
 'English-language_television_programming': -3.7104930477923213,
 'English_cricketers': -4.33886409286167,
 'English_footballers': -2.8820574639224525,
 'Fellows_of_the_Royal_Society': -3.9895935430971483,
 'French_films': -4.326116044867031,
 'German_footballers': -4.456736227284095,
 'Guggenheim_Fellows': -3.6888655005282134,
 'Harvard_University_alumni': -3.3278465172336955,
 'Hindi-language_films': -4.362666154141961,
 'Indian_films': -3.529281105125057,
 'Insects_of_Europe': -4.538584895115376,
 'Italian_films': -4.536845764242249,
 'Italian_footballers': -4.248295259256514,
 'Main_Belt_asteroids': -2.864690057561864,
 'Major_League_Baseball_pitchers': -3.4613779098582182,
 'Rivers_of_Romania': -3.2126024327392466,
 'Russian_footballers': -3.8849369695440146,
 'Scottish_footballers': -4.084702687568837,
 'Serie_A_players': -4.102269011286736,
 'The_Football_League_players': -2.7391669822712505,
 'Villages_in_Turkey': -7.499255860412547,
 'Villages_in_the_Czech_Republic': -3.6766612070381517,
 'Windows_games': -3.7696216409289414,
 'Yale_University_alumni': -4.1700570633508365}


c_linenum = None
correct = 0
total = 0
final_prob = {}

def sumDict(d1,d2):
        result = {key: float(d1[key]) + float(d2[key]) for key in d1}
        return result

for line in sys.stdin:
        line = line.strip()
        linenum, value = line.split('\t')
        line_dict = ast.literal_eval(value)
        if c_linenum == linenum:
                #print('max: ', max(final_prob, key = final_prob.get))
                final_prob = sumDict(final_prob, line_dict)
        else:
                if c_linenum:
                        lnum, labels = c_linenum.split('~')
                        correct_labels = labels.split(',')
                        final_prob = sumDict(final_prob, lab_prob_red)
                        pred_label = max(final_prob, key = final_prob.get)
                        if pred_label in correct_labels:
                                correct += 1
                        total += 1
                        
                        #print('linenum: ',lnum,'correct: ',correct_labels,'pred: ',pred_label)
                c_linenum = linenum
                final_prob = line_dict

if c_linenum == linenum:
        lnum, labels = c_linenum.split('~')
        correct_labels = labels.split(',')
        final_prob = sumDict(final_prob, lab_prob_red)
        pred_label = max(final_prob, key = final_prob.get)
        if pred_label in correct_labels:
                correct += 1
        total += 1
        #print('linenum: ',lnum,'correct: ',correct_labels,'pred: ',pred_label)
print('zz~total= ',total,'\t correct= ',correct)
