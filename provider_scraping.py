"""
Hattip to Greg Reda http://www.gregreda.com/2013/04/29/more-web-scraping-with-python/
"""

from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep
import csv

root = raw_input("Root url:")
url_params = raw_input("Url params:")
list_url = "http://" + root + "/" + url_params

soup = BeautifulSoup(urlopen(list_url).read())
providers = soup.find_all("a", class_="provider", href=True)
provider_urls = ["http://" + root + a["href"] for a in providers]

with open("data/providers.csv", "w") as f:
	fieldnames = ("name", "summary", "location", "service_areas", "homepage_url", "service_urls")
	output = csv.writer(f, delimiter=",")
	output.writerow(fieldnames)

	for url in provider_urls:
		soup = BeautifulSoup(urlopen(url).read())

		# === Get provider name === #
		name = soup.h1.string
		print "Getting data for %s \n" % name
		
		# === Get provider summary === #
		summary = soup.find_all(id="provider_description")

		# === Get provider location === #
		location_caption = soup.find(text="Headquarters")
		location = location_caption.find_next("td").string
		
		# === Get provider service areas === #
		service_areas_caption = soup.find(text="Service Areas")
		service_areas = service_areas_caption.find_next("td").string

		# === Get provider URL === #
		homepage_url = soup.find("a", class_="trackable", href=True).string

		# == Get provider services == #
		service_urls = [h3.a['href'] for h3 in soup.find_all('h3')]

		output.writerow([name, summary, location, service_areas, homepage_url, service_urls])
		sleep(1)

print "Done writing file"
