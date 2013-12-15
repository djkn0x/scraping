"""
Quick script thrown together to verify whether a user's last name appears in their 
email address. A quick, but extremely blunt, approach to confirm the email address is truly
associated with the user. Many, many false negatives using this approach.  

"""

import csv

filename = '/Users/dk/Dev/python_projects/data/fetch_1.csv'
ifile = csv.reader(open('%s' % filename, 'rb'), delimiter=",")
ofile = csv.writer(open('fetch_output.csv', 'wb'))

for row in ifile:

	first = row[0]
	middle = row[1]
	last = row[2]
	email = row[3]
	organization = row[4]
	admin_inst = row[5]
	activity = row[6]
	year = row[7]

	last_lower = last.lower()

	if last_lower in email:

		try:
			ofile.writerow([first, middle, last, email, organization, admin_inst, activity, year])
		except:
			pass

	else: 
		pass
