#!/usr/bin/python2.7
# Program to To split CSV line by line
import csv		

with open("sample.csv") as data:
	for index, line in enumerate(data):
		with open('sam{}.csv'.format(index), 'w') as fw:
			writer = csv.writer(fw, delimiter=',')
			writer.writerow([line])