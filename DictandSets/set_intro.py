farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
wild_animals = {'lion', 'elephant', 'horse', 'goat', 'gorilla'}

print(farm_animals)


for animal in farm_animals:
    print(animal)

print()
print("Indexing a sequence ")
animal_list = ['cow', 'sheep', 'hen', 'goat', 'horse'] 
goat = animal_list[4]
print(goat)

# print("indexing a set is not possible")
# goat = farm_animals[4]

more_animals = {'hen', 'cow', 'horse', 'sheep', 'goat' }
if more_animals == farm_animals:
    print('Set are equal')
else: 
    print('Set are not equal')
