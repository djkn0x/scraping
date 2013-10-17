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


# === Function to strip HTML tags (via http://stackoverflow.com/a/14603269/2874813) === #
def stripHtmlTags(htmlTxt):
    if not htmlTxt:
        return ''.join(BeautifulSoup(htmlTxt).find_all(text=True))
  

# === Writes provider output to .csv file === #
with open("data/providers.csv", "w") as f:
    fieldnames = ("name", "summary", "location", "service_areas", "homepage_url", "service_urls")
    output = csv.writer(f, delimiter=",")
    output.writerow(fieldnames)

    for url in provider_urls:
        try:
            soup = BeautifulSoup(urlopen(url).read())

            # === Get provider name === #
            name_html = soup.h1.encode('utf-8')
            name = stripHtmlTags(name_html)
            print "Getting data for %s \n" % name

            # === Get provider summary === #
            summary = soup.find_all(id="provider_description")

            # === Get provider location === #
            location_caption = soup.find(text="Headquarters")
            location_html = location_caption.find_next("td").encode('utf-8')
            location = stripHtmlTags(location_html)

            # === Get provider service areas === #
            service_areas_caption = soup.find(text="Service Areas")
            service_areas_html = service_areas_caption.find_next("td").encode('utf-8')
            service_areas = stripHtmlTags(service_areas_html)

            # === Get provider URL === #
            homepage_url_html = soup.find("a", class_="trackable", href=True).encode('utf-8')
            homepage_url = stripHtmlTags(homepage_url_html)

            # == Get provider services == #
            service_urls = [h3.a['href'] for h3 in soup.find_all('h3')]

            output.writerow([name, summary, location, service_areas, homepage_url, service_urls])

        except:
            pass

        sleep(1)

print "Done writing file"
