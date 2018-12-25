#sort_csv.py 

import sys, csv ,operator, re

with open('ratings.csv', 'r') as fin, open('ratings_filt.csv', 'w', newline='') as fout:

    # define reader and writer objects
    reader = csv.reader(fin, skipinitialspace=True)
    writer = csv.writer(fout, delimiter=',')

    # write headers
    writer.writerow(next(reader))

    # iterate and write rows based on condition
    for i in reader:
        if int(i[-1]) != -1:
            writer.writerow(i)