import csv 



with open(r'C:\xampp\htdocs\Python\TextFiles\OlympicMedals_2020.csv', encoding='utf-8', newline='') as data_files: 
        headers = data_files.readline().strip('\n').split(',')
        print(f'Columns headers:{headers}')
        medalsreader = csv.reader(data_files, delimiter=' ', quotechar='|' )
        for row in medalsreader: 
            print(','.join(row))