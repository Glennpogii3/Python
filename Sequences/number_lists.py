even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9] 

numbers = [odd, even] # lists of two lists inside
print(numbers) 

for number_list in numbers:
    print(number_list)
    
    for value in number_list:
        print(value)


# odd.extend(even) # Use to extend the list into another list
# print(odd)
# another_odd = odd 
# print(another_odd)

# odd.sort() # User to sort the list
# print(odd)


# odd.reverse() # User to Reverse  the list
# odd.sort(reverse=True) # Another way of reverse sorting
# print(odd)