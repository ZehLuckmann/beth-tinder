import csv

def csv_file(arq):
    with open(arq, 'r') as f:
        reader = csv.reader(f)
        return list(reader)
