import nltk
import pandas as pd
import numpy as np
import csv


from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

#select directory that contains Stanford Classifer and choose classifier, and also the 'stanford-ner.jar' file
st = StanfordNERTagger(
    '~/stanford-ner-2020-11-17/classifiers/english.all.3class.distsim.crf.ser.gz',
    '~/stanford-ner-2020-11-17/stanford-ner.jar',
    encoding='utf-8')

#Select directory to perform NER on
text = open(
    '/directory').read()

tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)

locations = []

# Code will go through all text files in the directory and pull out all LOCATIONS and add them to a csv
for i in classified_text:
    if i[1] == "LOCATION": # Can replace Location with, Person etc. dependent on classifier.
        locations.append(i)

print(locations)



