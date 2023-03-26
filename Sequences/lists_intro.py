computer_parts = ["Cpu", 
                  "monitor", 
                  "mouse", 
                  "keyboard", 
                  "mouse mat",
                  "headset"
                  ]

print(computer_parts)



# for part in computer_parts:
#     print(part) # 

# print()
# print(computer_parts[2]) # computer parts index 2
# print(computer_parts[0:3]) #  computer parts index 0 to 3 
# print(computer_parts[-1]) # computer parts index  negative starts at the last of list


flowers = [["rose", "red"],
           ["snapdragon", "white"],
           ["daisy", "white"],
           ["lily", "yellow"]
           ]
 
second_flowers = flowers
 
second_flowers[1] = ["lilac", 'purple']
 
second_flowers[1][1] = 'pink'
print(flowers)


numbers = range(13)
 
new_range = numbers[1::2]
for i in new_range:
    print(i, end=', ')
    
    
imelda = 'More Mayhem', 'Imelda May', 2011, [
    (1, 'Pulling the Rug'),
    (2, 'Psycho'),
    (3, 'Mayhem'),
    (4, 'Kentish Town Waltz')]
 
imelda[3].append(5, 'All For You')
print(imelda[3])