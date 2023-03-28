import csv

countries = {}
dialect = csv.excel
dialect.delimiter = '|'


with open(r'C:\xampp\htdocs\Python\TextFiles\country_info.txt', 'r', encoding='utf-8', newline='')  as country_file:
   
    headings = country_file.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()
    
    #country_file.readline()
    
    dict_reader = csv.DictReader(country_file, dialect=dialect, fieldnames=headings)
    for row in dict_reader:
        # data = row.strip('\n').split('|')
        # country, capital, code, code3, dialing, timezone, currency = data
        # # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        # country_dict = {
        #     'name': country,
        #     'capital': capital,
        #     'country_code': code,
        #     'cc3': code3,
        #     'dialing_code': dialing,
        #     'timezone': timezone,
        #     'currency': currency,
        # }
        # print(country_dict)
        #countries[country.casefold()] = country_dict
        #countries[code.casefold()] = country_dict
        
        countries[row['country'].casefold()] = row
        countries[row['cc'].casefold()] = row
        
# print(countries)

while True:
    chosen_country = input('Please enter the name of a country: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif chosen_country == 'quit':
        break
