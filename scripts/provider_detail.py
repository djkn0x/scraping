from bs4 import BeautifulSoup
import urllib2

root = raw_input("Root url:")
params = raw_input("Provider params:")

print "\n...Retrieving info for %s \n" % params

url = "http://" + root + "/providers/" + params
file = urllib2.urlopen(url)
soup = BeautifulSoup(file)

# === Function to strip HTML tags (via http://stackoverflow.com/a/14603269/2874813) === #
def stripHtmlTags(htmlTxt):
	if htmlTxt is None:
		return None
	else:
		return ''.join(BeautifulSoup(htmlTxt).find_all(text=True))


# === Get provider name === #
name_html = soup.h1.encode('utf-8')
name = stripHtmlTags(name_html)
print "Name: %s \n" % name

# === Get provider summary === #
summary = soup.find_all(id="provider_description")
print "Summary: %s \n" % summary

# === Get provider location === #
location_caption = soup.find(text="Headquarters")
location_html = location_caption.find_next("td").encode('utf-8')
location = stripHtmlTags(location_html)
print "Location: %s \n" % location

# === Get provider service areas === #
service_areas_caption = soup.find(text="Service Areas")
service_areas_html = service_areas_caption.find_next("td").encode('utf-8')
service_areas = stripHtmlTags(service_areas_html)
print "Service Areas: %s \n" % service_areas

# === Get provider URL === #
homepage_url_html = soup.find("a", class_="trackable", href=True).encode('utf-8')
homepage_url = stripHtmlTags(homepage_url_html)
print "URL: %s \n" % provider_url

# == Get provider services == #
service_url = [h3.a['href'] for h3 in soup.find_all('h3')]
print service_url
