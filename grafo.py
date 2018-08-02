#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 23:28:22 2018

@author: eduardodutra
"""

import csv
from glob import glob

candidatos = dict([])
full_word_list = []

for filename in glob('out/pyspark*.csv'):
    print(filename)
    candidato = filename.split('_')[2].split('.')[0]
    with open(filename, newline='\r\n', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        data = dict(reader)
        del data['Word']
        candidatos[candidato] = data
        full_word_list = list(set(full_word_list + list(data.keys())))

full_word_list = list(full_word_list.sort())

keys = list(candidatos.keys())
grafo = [['palavra']+keys]

for word in full_word_list:
    row = [word]
    for cand in candidatos:
        row.append(candidatos[cand].get(word,None))
    grafo.append(row)
    
with open('out/grafo.csv', 'w', encoding='utf-8') as f: 
    csv_out=csv.writer(f)
    csv_out.writerows(grafo)
