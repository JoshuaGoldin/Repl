import urllib2
from bs4 import BeautifulSoup
import builtwith
qoute_page="https://business.gwu.edu/faculty-directory"
req = urllib2.Request(qoute_page, headers={'User-Agent' : "Magic Browser"}) 
con = urllib2.urlopen( req )
soup = BeautifulSoup(con, 'html.parser')
faculty=[]
phd=[]
for i in range(len(soup.find_all('a'))):
  if ',' in soup.find_all('a')[i].text:
    faculty.append(soup.find_all('a')[i].text)
print len(faculty)
print "Faculty", faculty
for i in range(len(faculty)):
  abbrev=faculty[i].split(',')[1][2:]+"-"+faculty[i].split(',')[0][2:]
  abbrev1=abbrev
  abbrev1=abbrev.split('.')[0]
  if "Mehmet" in abbrev1:
    abbrev1="mehmet-sekip-altug"
  if "Artz" in abbrev1:
    abbrev1="john-m-artz"
  if "Bailey" in abbrev1:
    abbrev1="james-r-bailey"
  if "Ballesteros" in abbrev1:
    abbrev1="luis-ballesteros"
  if "Baptista" in abbrev1:
    abbrev1="alexandre-m-baptista"
  if "Carayannis" in abbrev1:
    abbrev1="elias-g-carayannis"
  prof_url='http://www.bschool.howard.edu/go/about/faculty/profile.html?id=amayse'
  if abbrev1=='dcogburn':
    prof_url='https://business.gwu.edu/'+abbrev1
  qoute_page="https://business.gwu.edu/"+abbrev1
  print qoute_page
  req = urllib2.Request(qoute_page, headers={'User-Agent' : "Magic Browser"}) 
  con = urllib2.urlopen( req )
  soup = BeautifulSoup(con, 'html.parser')
  phd=[]
  if 'Ph.D' in soup.text:
    phd.append(abbrev1)
    print abbrev1 + " has a Ph.D."
  else:
    print abbrev1 + " does not have a Ph.D."
  print phd
