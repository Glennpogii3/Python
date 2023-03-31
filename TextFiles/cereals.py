import csv 

file_path = 'cereal_grains.csv'

with open(file_path, encoding='utf-8', newline='') as csv_file:
    read_cereal = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in read_cereal:
        print(row)
