# csvsplitter
#A pyhton program to split a CSV File line by line and save each line into a separate CSV file 
#!/usr/bin/python2.7

import csv		

with open("sample.csv") as data:
	for index, line in enumerate(data):
		with open('sam{}.csv'.format(index), 'w') as fw:
			writer = csv.writer(fw, delimiter=',')
			writer.writerow([line])
