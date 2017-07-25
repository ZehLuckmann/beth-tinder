import csv

def get_csv_file(arq):
    with open(arq, 'r') as f:
        reader = csv.reader(f)
        return list(reader)

def write_csv_file(arq, data):
    with open(arq, 'w') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL)
        for r in data:
            wr.writerow(r)
