import json

languages = [
    ('ABC', 1987),
    ('Algol 68', 1968),
    ('APL', 1962),
    ('C', 1973),
    ('Haskell', 1990),
    ('Lisp', 1958),
    ('Modula-2', 1977),
    ('Perl', 1987),
]

# with open(r'C:\xampp\htdocs\Python\TextFiles\test.json', 'w', encoding='utf-8') as json_file:
#     json.dump(languages, json_file)

with open(r'C:\xampp\htdocs\Python\TextFiles\test.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

print(data)
print(data[3])