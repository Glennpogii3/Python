numbers = set()
# numbers ={*""}
# numbers ={*{}}

print(numbers, type(numbers))
# numbers.add(1)
# print(numbers)

# while len(numbers) < 4:  # max input of 4 length. 
#     next_value = int(input("Please enter your next value: "))
#     numbers.add(next_value)
# print(numbers)
    
data = ["blue", "green", "yellow", "blue", "green", "yellow", "white"]

#Create a set from the list, to remove duplicates
unique_data = sorted(set(data))
print(unique_data)

# Create a list of unique colours, keeping the order they appeared 
unique_data = list(dict.fromkeys(data))
print(unique_data)


print()
print()
print(dict.fromkeys(data))