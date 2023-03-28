import csv


with open(r'C:\xampp\htdocs\Python\TextFiles\country_info.txt', 'r', encoding='utf-8', newline='') as countries_data:
    sample = ""
    for line in range(3): 
        sample += countries_data.readline()
    country_dialect = csv.Sniffer().sniff(sample)
    country_dialect.skipinitialspace = True
    countries_data.seek(0)
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)

print("*" * 100)
attributes = [
    'delimiter',
    'doublequote',
    'escapechar',
    'lineterminator',
    'quotechar',
    'quoting',
    'skipinitialspace',
]


for  attribute in attributes: 
    print(f'{attribute}: {repr(getattr(country_dialect, attribute))}') 