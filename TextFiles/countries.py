
countries = {}
code_lookup = {}
file_path = 'country_info.txt'

with open(file_path, 'r') as countries_data:
    countries_data.readline()
    for row in countries_data: 
        data = row.strip('\n').split('|') 
        # data = row.split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n \t')

        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code, 
            'cc3': code3,
            'dialing_code': dialing, 
            'timezone': timezone,   
            'currency': currency, 
        }
        
#       print(country_dict)
        countries[country.casefold()] = country_dict
#       code_lookup = [code.casefold()] = country
        countries[code.casefold()] = country_dict 

while True:
    country_choice = input("Please enter the name of the a country: ").casefold()
    country_key = country_choice.casefold()
    if country_key in countries:
        country_data = countries[country_key] 
        print(f"The capital of the {country_choice} is {country_data['capital']}")
    elif country_choice == '0':
        break
