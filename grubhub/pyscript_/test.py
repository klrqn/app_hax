import csv

with open('addy.csv', newline='') as csvfile:
    aList = []
    filereader = csv.reader(csvfile, delimiter = '\t', quotechar = '|')
    for row in filereader:
        aList = aList + row

print(aList)
