import csv 


with open(r'C:\xampp\htdocs\Python\TextFiles\cereal_grains.csv', encoding='utf-8', newline='') as csv_file: 
    read_cereal = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in read_cereal:
        print(row)