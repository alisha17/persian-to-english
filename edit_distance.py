# -*- coding: utf-8 -*-
from __future__ import division
from Levenshtein import distance
import json
from random import randint
# import distance

dict1 = dict()
l1 = list()
mydict = dict()
my_dict = dict()
new = dict()

# Blosum matrix
vowels = ['a','e','h','i','o','u','w','y']
labials = ['b','p','f','v']
misc = ['c','g','j','k','q','s','x','z']
dentals = ['d','t']
lateral = ['l']
nasal = ['m','n']
rhotic = ['r']

def equal(a,b):
	if a == b :
		return 0
	elif (a and b) in (vowels, labials, misc, dentals, lateral, nasal, rhotic) :
			return 1
	else:
		return randint(2,9)

def matchWords(s1, s2):
    m=len(s1)+1
    n=len(s2)+1
    i = -1
    j = -1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+equal(s1[i-1],s2[j-1]))

    return tbl[i,j]

with open('/home/alisha/Desktop/KT/2017S1-90049P1-data-dos/train.txt') as f:
	#persian names with their equivalent latin name
	for line in f:
		b = " ".join(line.split())
		b = b.split(" ")
		dict1.update({b[0].lower():b[1]})

with open('/home/alisha/Desktop/KT/2017S1-90049P1-data-dos/names.txt') as f:
	#latin names
	for line in f:
		line = line.strip()
		l1.append(line)

for ke in dict1.keys():
    temp_dict = dict()
    for index, item in enumerate(l1):
        if (item == ""):
            break
        # edit_dist = distance.jaccard(ke, item)
        # edit_dist = matchWords(ke, item)
        edit_dist = distance(ke, item)
        if (edit_dist in temp_dict):
            temp_dict[edit_dist].append(item)
        else:
            temp_dict[edit_dist] = [item]
    new[ke] = temp_dict

for key, value in new.iteritems():
    min_dist = list(min(key for key in value.iteritems()))
    my_dict[key] = min_dist

recall = 0
totalprecision = 0
no_of_correct_responses = 0
length = 0

for key, value in dict1.iteritems():
    if key in my_dict:
        length = length + len(my_dict[key][1])
        distance, item = my_dict[key][0], my_dict[key][1]

        check = filter(lambda element: value in element, item)

        if len(check) > 0:
            no_of_correct_latin_word = 1
        else:
            no_of_correct_latin_word = 0
        my_dict[key].append({"correct_latin_word_count" : no_of_correct_latin_word})

for key,value in my_dict.iteritems():
	no_of_correct_responses  = no_of_correct_responses + sum(v for k,v in value[2].iteritems())
	totalprecision = (no_of_correct_responses/length)

	if value[2]["correct_latin_word_count"] != 0:
		recall = recall + 1

totalrecall = recall / len(my_dict)*(100)
print "Recall is",totalrecall,"%"
print "Precision is",totalprecision*100,"%"

with open('edited.txt','w') as fout:
    fout.write(json.dumps(my_dict,indent=4))










