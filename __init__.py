__author__ = 'Manitra.Rakotozafy'

import csv
reader = csv.DictReader(open('../data/congress-clean.csv'))

sampleBase = []
for row in reader:
    sampleBase.append(row)

print sampleBase
