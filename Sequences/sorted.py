pangram = "The quick brown fox jumped over the lazy dog"


letters = sorted(pangram)
print(letters)

numbers = [1.1, 23, 1.2, 1.3, 1.4, 1.5, 1.6]

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

missing_letters = sorted("The quick brown fox jumped over the lazy dog",
                         key=str.casefold)
print(missing_letters)


names = ["Joyce", 
         "Glenn",
         "terry",
         "Francis",
         "Bob",
         "mary"
         ]

names.sort(key=str.casefold)
print(names)