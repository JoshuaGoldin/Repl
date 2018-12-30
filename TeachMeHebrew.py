#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#Author: Joshua Goldin
#Compiler: Repl.it
import os, sys
import urllib2
import time
import csv
import unicodedata
from bs4 import BeautifulSoup
qoute_page='https://www.teachmehebrew.com/500-basic-hebrew-words.html'
page= urllib2.urlopen(qoute_page)
soup = BeautifulSoup(page, 'html.parser')
trans={}
t=[]
trans.update({"eat":"לאכול".decode("UTF-8")})
start_time = time.time()
for j in range (250):
  for i in range(2):
    att="alt"+str(i+1)
    p=soup.find_all('tr', attrs={'class': att})
    if ('\t' in p[j].text.strip()):
      word=p[j].text.strip().split('\t')
    trans.update({word[0]:word[len(word)-1]})
    t.append(word[0])
#Getting the english and the hebrew spelling of the words
print trans["I"], trans["eat"],trans["apple"], ": hello I"
print trans['I'], 'ה'.decode('UTF-8')+trans['apple'], ": I eat apple "
with open('hebrew.txt', 'w') as f:
    for i in range (250):
      f.write(t[i].encode("UTF-8")+","+trans[t[i]].encode('UTF-8')+"\n")
print("--- %s seconds ---" % (time.time() - start_time))
