#Author: Joshua Goldin
#Compiler: Repl.it
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
for j in range (250):
  for i in range(2):
    att="alt"+str(i+1)
    p=soup.find_all('tr', attrs={'class': att})
    if ('\t' in p[j].text.strip()):
      word=p[j].text.strip().split('\t')
    trans.update({word[0]:word[len(word)-1]})
    t.append(word[0])
#lines 13-20 Getting the english and the hebrew spelling of the words
print trans['hello'], trans["I"], ": hello I"
print trans['I'], trans['apple'], ": I apple "
with open('some.csv', 'w') as f:
    writer = csv.writer(f)
    for i in range (250):
      trans[t[i]]=trans[t[i]].encode('cp424')
      writer.writerow(trans[t[i]])
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
