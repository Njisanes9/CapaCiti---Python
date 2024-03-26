
import csv

f = open('First_File.csv', 'r')


with open('First_File.csv', 'r' ) as r:
    reader = csv.reader(r, delimiter='\t')
    for row in reader:
        print(row)
