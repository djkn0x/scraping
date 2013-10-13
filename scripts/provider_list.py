from bs4 import BeautifulSoup
import urllib2

root = raw_input("Root url:")
search_params = raw_input("Url params:")

print "...Retrieving provider urls"

url = "http://" + root + "/" + search_params
file = urllib2.urlopen(url)
soup = BeautifulSoup(file)

sAll = soup.findAll("a", class_="provider", href=True)

for a in sAll: 
	print "http://" + root + a['href']
