import urllib2
import time
import csv
import unicodedata
from bs4 import BeautifulSoup
date=120101
for i in range(2190):
  date+=1
  if date % 100 == 31:
    if ((date-(date / 10000)*10000)-(date % 100))/100== 12:
      date+=8900
    date+=69
  try:
    qoute_page='https://www.spc.noaa.gov/climo/reports/'+str(date)+'_rpts.html'
  except urllib2.HTTPError as err:
    pass
  try:
    page= urllib2.urlopen(qoute_page)
  except urllib2.HTTPError as err:
    #print err.code
    pass
  soup = BeautifulSoup(page, 'html.parser')
  f = open('Damages from Weather.txt', 'wb')
  for i in range(len(soup.find_all('td', attrs={'class':'rpttext'}))):
    if "DAMAGE" in soup.find_all('td', attrs={'class':'rpttext'})[i].text:
      print "choose", soup.find_all('td', attrs={'class':'rpttext'})[i].text, date
      print
      f.write(soup.find_all('td', attrs={'class': 'rpttext'})[i].text+ "\n")
      pass
#put the text into a csv file
