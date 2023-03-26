empty_list = []

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9] 


numbers = odd + even 
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)


digits = sorted("987651234")
print(digits)

# more_numbers = list(numbers)
#more_numbers = numbers[:] 
more_numbers = numbers.copy()
print(more_numbers)
print(numbers is more_numbers)
print(id(numbers))
print(id(more_numbers))
print(numbers == more_numbers)