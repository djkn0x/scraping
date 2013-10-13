from bs4 import BeautifulSoup
import urllib2

root = raw_input("Root url:")
params = raw_input("Provider params:")

print "\n...Retrieving info for %s \n" % params

url = "http://" + root + "/providers/" + params
file = urllib2.urlopen(url)
soup = BeautifulSoup(file)


# === Get provider name === #
name = soup.h1.string
print "Name: %s \n" % name

# === Get provider summary === #
summary = soup.find_all(id="provider_description")
print "Summary: %s \n" % summary

# === Get provider location === #
location_caption = soup.find(text="Headquarters")
location = location_caption.find_next("td").string
print "Location: %s \n" % location

# === Get provider service areas === #
service_areas_caption = soup.find(text="Service Areas")
service_areas = service_areas_caption.find_next("td").string
print "Service Areas: %s \n" % service_areas

# === Get provider URL === #
provider_url = soup.find("a", class_="trackable", href=True).string
print "URL: %s \n" % provider_url

# == Get provider services == #
service_url = [h3.a['href'] for h3 in soup.find_all('h3')]
print service_url
