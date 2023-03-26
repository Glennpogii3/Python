# parrot = "Norwegian Krone"

# for character in parrot: 
#      print(character)
     

number = input("Enter a sequence number")
seperators = ""

for char in number: 
    if not char.isnumeric(): 
        seperators = seperators + char
# print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split() 
print(sum([int(val) for val in values]))
