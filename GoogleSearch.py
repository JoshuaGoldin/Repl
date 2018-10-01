import urllib2
from bs4 import BeautifulSoup
import re
qoute_page='https://www.google.com/search?q=newyorkcity+cybersecurity+reporter&num=100'
req = urllib2.Request(qoute_page, headers={'User-Agent' : "Magic Browser"}) 
con = urllib2.urlopen( req )
soup = BeautifulSoup(con, 'html.parser')
urls=[]
for i in range (len(soup.find_all('a'))):
  if 'search' not in (soup.find_all('a')[i].attrs['href']) and 'google' not in (soup.find_all('a')[i].attrs['href']) and 'q=' in (soup.find_all('a')[i].attrs['href']):
    url=soup.find_all('a')[i].attrs['href'].split('=')[1].split('&')[0]
    urls.append(url)
for i in range(len(urls)):
  qoute_page=urls[i]
  req = urllib2.Request(qoute_page, headers={'User-Agent' : "Magic Browser"})
  try:
    con = urllib2.urlopen(req)
  except urllib2.HTTPError as httperr:
    pass
  soup = BeautifulSoup(con, 'html.parser')
  if "name" in soup.text:
    print urls[i]
