import csv
from bs4 import BeautifulSoup
import nltk

# directory as input
# filename as input

def main():
	reader = csv.reader(open('summary.csv', 'rU'))
	writer = csv.writer(open('summaryProcessed.csv', 'wb'))

	for row in reader:
		# Convert to string
		row = str(row)
		row = row.decode('utf8')
		
		# Remove HTML
		soup = BeautifulSoup(row)
		text = soup.find_all(text=True)
		
		# Tokenize
		text = str(text)
		name = {}
		a = nltk.wordpunct_tokenize(text)
		b = nltk.pos_tag(a)
		c = nltk.ne_chunk(b, binary=True)
		for x in c.subtrees():
			if x.node == "NE":
				words = [w[0] for w in x.leaves()]
				name = " ".join(words)
				print name
		
		writer.writerow([name])


if __name__=="__main__":
	main()
