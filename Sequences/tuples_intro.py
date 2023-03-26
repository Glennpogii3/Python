albums = [("Welcome to my Nightmare", "Alice Cooper", 1975), 
        ("Bad Company", "Bad Company", 1974),
        ("Night Flight", "Budgie", 1981),
        ("More Maynem", "Emilda May", 2011),
        ("Ride the Lighting", "Metallica", 1984) 
        ]

print(len(albums))

# for album in albums:
#     print("Album: {}, Artist {}, Year: {}"
#           .format(album[0], album[1], album[2]))
# for name, artist, year in albums:
#     print("Album: {}, Artist: {}, Year: {}"
#           .format(name, artist, year))

for album in albums:
    name, artist, year = albums
    print("Album: {}, Artist {}, Year: {}"
          .format(name, artist, year))








# print(metallica) # Tuple 
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

# metallica2 = list(metallica) # Change into a list.
# print(metallica2)

# metallica2[0] = "Welcome to my World"
# print(metallica2)

# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)

# table = ("Coffee table", 200, 100, 45, 23.34)
# print(table[1] * table[2])

# name, length, width, height, price = table 
# print(length * width)
