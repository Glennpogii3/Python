import csv

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

keys = ['album', 'artist', 'year']


with open(r'C:\xampp\htdocs\Python\TextFiles\albums.csv', 'w',  encoding='utf-8', newline='') as data_file:
    writer = csv.DictWriter(data_file, fieldnames=keys, extrasaction='ignore')
    writer.writeheader()
    for row in albums: 
        zip_object = zip(keys, row)
        # print(zip_object)
        # for thing in zip_object:
        #     print(thing)
        
        albums_dict = dict(zip_object)
        print(albums_dict)
        writer.writerow(albums_dict)
    
    # for row in medals_table:
    #     writer.writerow(row)
    