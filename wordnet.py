# -*- coding: utf-8 -*-
"""WordNet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HoHVHNtNDgLuJW-0oYK-DSRfbjgbq0x2
"""

import nltk
from nltk.corpus import wordnet as wn
import numpy as np
import pandas as pd

nltk.download('wordnet')

verbs = pd.read_csv('VerbsOutput.csv', header=None)
verbs0 = verbs.to_numpy()
verbs = []
for verb in verbs0:
  verbs.append(verb[0])
print(verbs)

def giveName(input):
  input = str(input)
  return input[9 : -3]

synonymOutput = []
for verb in verbs:
  syns = []
  for synonym in wn.synsets(verb):
      syns.append(synonym.lemmas()[0].name())
  syns = list(dict.fromkeys(syns))
  result = 'Synonyms of "' + verb + '" are: '
  for syn in syns:
    result += syn +', '
  if syns:
    result = result[ 0:-2]
  else:
    result += '___'
  synonymOutput.append(result)

with open("/content/drive/MyDrive/Colab Files/Wordnet/Synonyms.txt", "w") as txt_file:
    for line in synonymOutput:
        txt_file.write( line + "\n")

for i in synonymOutput:
  print(i)

hypernymOutput = []
for verb in verbs:
  for ss in wn.synsets(verb):
    result = 'hypernym of "' + verb + '" for it\'s sense "' + ss.name() + '" is: '
    hyper = ss.hypernyms()
    if hyper:
      result += giveName(hyper)
    else:
      result+= '___'
    hypernymOutput.append(result)

with open("/content/drive/MyDrive/Colab Files/Wordnet/Hypernyms.txt", "w") as txt_file:
    for line in hypernymOutput:
        txt_file.write( line + "\n")

for i in hypernymOutput:
  print(i)

hyponymOutput = []
for verb in verbs:   
  for ss in wn.synsets(verb):
    result = 'hyponyms of "' + verb + '" for it\'s sense "' + ss.name() + '" are: '
    hypos = ss.hyponyms()
    for hypo in hypos:
      result += hypo.name() + ", "
    if hypos:
      result = result[0: -2]
    else:
      result += '___'
    hyponymOutput.append(result)

with open("/content/drive/MyDrive/Colab Files/Wordnet/Hyponyms.txt", "w") as txt_file:
    for line in hyponymOutput:
        txt_file.write( line + "\n")

for i in hyponymOutput:
  print(i)

lch_sim = []
for i in range(len(verbs)):
  for j in range(i+1 , len(verbs)):
    first = wn.synsets(verbs[i], pos=wn.VERB)
    second = wn.synsets(verbs[j], pos=wn.VERB)
    result = 'Leacock Chodorow similarity for "' + verbs[i] + '" and "' + verbs[j] + '"\n'
    for sense1 in first:
      for sense2 in second:
        result += ( 'between the sense "' + sense1.name() + '" and "' + sense2.name() + '" is: ' + str(sense1.lch_similarity(sense2)) + '\n')
    lch_sim.append(result)

with open("/content/drive/MyDrive/Colab Files/Wordnet/lch_similarity.txt", "w") as txt_file:
    for line in lch_sim:
        txt_file.write( line + "\n")

print(lch_sim[0])

wup_sim = []
for i in range(len(verbs)):
  for j in range(i+1 , len(verbs)):
    first = wn.synsets(verbs[i])
    second = wn.synsets(verbs[j])
    result = 'Wu-Palmer similarity for "' + verbs[i] + '" and "' + verbs[j] + '"\n'
    for sense1 in first:
      for sense2 in second:
        result += ( 'between the sense "' + sense1.name() + '" and "' + sense2.name() + '" is: ' + str(sense1.wup_similarity(sense2)) + '\n')
    wup_sim.append(result)

with open("/content/drive/MyDrive/Colab Files/Wordnet/wup_similarity.txt", "w") as txt_file:
    for line in wup_sim:
        txt_file.write( line + "\n")

print(wup_sim[0])

path_sim = []
for i in range(len(verbs)):
  for j in range(i+1 , len(verbs)):
    first = wn.synsets(verbs[i])
    second = wn.synsets(verbs[j])
    result = 'Path similarity for "' + verbs[i] + '" and "' + verbs[j] + '"\n'
    for sense1 in first:
      for sense2 in second:
        result += ( 'between the sense "' + sense1.name() + '" and "' + sense2.name() + '" is: ' + str(sense1.path_similarity(sense2)) + '\n')
    path_sim.append(result)

with open("/content/drive/MyDrive/Colab Files/Wordnet/path_similarity.txt", "w") as txt_file:
    for line in path_sim:
        txt_file.write( line + "\n")

print(path_sim[0])

sem_distance = []
for i in range(len(verbs)):
  for j in range(i+1 , len(verbs)):
    first = wn.synsets(verbs[i])
    second = wn.synsets(verbs[j])
    result = 'Semantic distance for "' + verbs[i] + '" and "' + verbs[j] + '"\n'
    for sense1 in first:
      for sense2 in second:
        result += ( 'between the sense "' + sense1.name() + '" and "' + sense2.name() + '" is: ' + str(sense1.shortest_path_distance(sense2)) + '\n')
    sem_distance.append(result)

with open("/content/drive/MyDrive/Colab Files/Wordnet/semantic_distance.txt", "w") as txt_file:
    for line in sem_distance:
        txt_file.write( line + "\n")

print(sem_distance[0])