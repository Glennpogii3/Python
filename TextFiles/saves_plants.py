data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# plants_filename = "flowers_print.txt"

# with open(r'C:\xampp\htdocs\Python\TextFiles\flowers_print.txt', "w") as plants:
#     for plant in data:
#         print(plant, file=plants)

# new_list = []
# with open(r'C:\xampp\htdocs\Python\TextFiles\flowers_print.txt') as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip())

# print(new_list)

# plants_filename = "flowers_write.txt" # the directory is not properly working 

# with open(r'C:\xampp\htdocs\Python\TextFiles\flowers_write.txt', "w") as plants:
#     for plant in data:
#         plants.write(plant)



# print(data)
# string_representation = data.__str__()
# print(type(string_representation))

#filename = "test_numbers.txt"
# with open(r'C:\xampp\htdocs\Python\TextFiles\test_numbers.txt', "w") as test:
#     for i in range(10):
#         print(i, file=test)

with open(r'C:\xampp\htdocs\Python\TextFiles\test_numbers.txt', "w") as test:
    for i in range(10):
        test.write(str(i) + "\n")
