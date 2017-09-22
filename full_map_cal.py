#!/usr/bin/env python
import sys
import ast
import math

lab_wcount_map = {'American_comedy_films': 91155,
 'American_drama_films': 130908,
 'American_film_actresses': 285558,
 'American_film_directors': 177187,
 'American_films': 622249,
 'American_male_film_actors': 415655,
 'American_male_television_actors': 349810,
 'American_military_personnel_of_World_War_II': 294954,
 'American_people_of_Irish_descent': 226387,
 'American_television_actresses': 242812,
 'Arctiidae': 5874,
 'Articles_containing_video_clips': 456349,
 'Association_football_defenders': 261278,
 'Association_football_forwards': 302317,
 'Association_football_goalkeepers': 156963,
 'Association_football_midfielders': 305756,
 'Asteroids_named_for_people': 90679,
 'Australian_rules_footballers_from_Victoria_(Australia)': 158889,
 'Black-and-white_films': 394502,
 'Brazilian_footballers': 82606,
 'British_films': 214924,
 'Columbia_University_alumni': 222765,
 'Deaths_from_myocardial_infarction': 243079,
 'English-language_albums': 360869,
 'English-language_films': 1006865,
 'English-language_journals': 121452,
 'English-language_television_programming': 321389,
 'English_cricketers': 152305,
 'English_footballers': 508462,
 'Fellows_of_the_Royal_Society': 229284,
 'French_films': 103319,
 'German_footballers': 60480,
 'Guggenheim_Fellows': 331038,
 'Harvard_University_alumni': 482387,
 'Hindi-language_films': 108776,
 'Indian_films': 237272,
 'Insects_of_Europe': 96714,
 'Italian_films': 66448,
 'Italian_footballers': 69170,
 'Main_Belt_asteroids': 171321,
 'Major_League_Baseball_pitchers': 377660,
 'Rivers_of_Romania': 60509,
 'Russian_footballers': 82505,
 'Scottish_footballers': 156903,
 'Serie_A_players': 105167,
 'The_Football_League_players': 566615,
 'Villages_in_Turkey': 4303,
 'Villages_in_the_Czech_Republic': 132858,
 'Windows_games': 297047,
 'Yale_University_alumni': 196756}

#nonzero = 0.00001
uni_word = 256278

for line in sys.stdin:
        mw_prob = {}
        line = line.strip()
        linenum, value = line.split('\t')
        mw_dict = ast.literal_eval(value)
        for label_key in lab_wcount_map:
                if label_key in mw_dict:
                        mw_prob[label_key] = math.log((int(mw_dict[label_key]))*1.0/(int(lab_wcount_map[label_key])+uni_word))
                else:
                        mw_prob[label_key] = math.log(1.0/(int(lab_wcount_map[label_key])+uni_word))
        print('{0}\t{1}'.format(linenum, mw_prob))
