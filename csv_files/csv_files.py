import csv

exam_results = []

with open("exam_results.csv") as csv_file:
    reader = csv.reader(csv_file)
     