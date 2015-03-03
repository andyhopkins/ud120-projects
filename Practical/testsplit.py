# -*- coding: utf-8 -*-
"""
Created on Tue Mar 03 22:18:26 2015

@author: Andy
"""

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
result = []

string = 'Hi Everyone  If you can read this message youre properly using parseOutText  Please proceed to the next part of the project'

words = string.split()

for word in words:
    result.append(stemmer.stem(word))
print ' '.join(result)
    

