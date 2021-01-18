#encoding:utf-8
import json
import pandas as pd
from tqdm import tqdm
import random
from PMI import *
import os
from extract import extract

in_file = open('train_base.json','r')
documents = []
count = 0

for line in in_file:
    line = line.strip()
    line = json.loads(line)
    content = line['content']
    print(content)
    extractwords = []
    words = extract(content)
    for word in words:
        extractwords.append(word)
    documents.append(set(extractwords))
    count += 1
    if count == 1000:
        break

pm = PMI(documents)
pmi = pm.get_pmi()
PMI_word = dict()
for p in tqdm(pmi):
    if pmi[p] > 10:
        word1,word2 = p.split(',')
        if word1 not in PMI_word.keys():
            PMI_word[word1] = [word2]
        else:
            PMI_word[word1].append(word2)

        if word2 not in PMI_word.keys():
            PMI_word[word2] = [word1]
        else:
            PMI_word[word2].append(word1)

with open('PMI_word.json','w',encoding='utf-8') as f:
    json.dump(PMI_word,f)