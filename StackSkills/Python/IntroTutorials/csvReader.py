import csv

with open('MASurveyReport_1.13.19.csv', newline='') as csvfile:
    getData = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in getData:
        print(', '.join(row))
