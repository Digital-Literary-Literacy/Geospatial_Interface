import nltk
import pandas as pd
import numpy as np
import csv


from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

st = StanfordNERTagger(
    '/Users/fiannualamorgan/Documents/stanford-ner-2020-11-17/classifiers/english.all.3class.distsim.crf.ser.gz',
    '/Users/fiannualamorgan/Documents/stanford-ner-2020-11-17/stanford-ner.jar',
    encoding='utf-8')

text = open(
    '/Users/fiannualamorgan/Documents/GitHub/Text_to_Test_for_Hugh/The_Golden_South_extract_unannotated.txt').read()

tokenized_text = word_tokenize(text)
classified_text = st.tag(tokenized_text)

locations = []

for i in classified_text:
    if i[1] == "LOCATION": #Replace Location with, Person etc
        locations.append(i)

print(locations)


# print("csv written")
