import csv 



with  open(r'C:\xampp\htdocs\Python\TextFiles\cereal_grains.csv', encoding='utf-8', newline='') as data_file:
    reader = csv.DictReader(data_file)
    for row in reader:
        print(row)