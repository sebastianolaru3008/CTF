# !/usr/bin/env python

import sys
import codecs


text = open(sys.argv[1], 'r').read()

size = len(text)
text = codecs.encode(text, 'rot_13')

count = 0
i = 0

list_of_sent = []
reverse = False
fcount = 0
sentence = ""

while i < size:
	if(fcount == 48):
		list_of_sent.append(sentence)
		sentence = ""
	
	if(text[i] == '\n'):
		rev_sentence = sentence[::-1]
		list_of_sent.append(rev_sentence)
		sentence = ""
		fcount = 0

	sentence+= text[i]
	fcount +=1
	i+=1

for l in list_of_sent:
	print l


