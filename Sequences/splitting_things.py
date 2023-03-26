# panagram = """The quick brown 
# fox jumpes\tover 
# the lazy dog"""

# words = panagram.split()

# print(words)


# numbers = "123,41235,123,1235,34,63,654,8765,945"
# print(numbers.split(","))

data = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]


print(data)

#Solution 4  list Compression
print([int(index) for index in data])


# Solution 3 List Compression + eval  
ints = [eval(index) for index in data]
print(ints)


# Solution 1  replace the values in the places For loop
# for index in range(len(data)):
#     data[index] = int(data[index])

# print(data)

# Solution 2 replace the values in the places For loop

# ints = []
# for number in data: 
#     ints.append(int(number))

# print(ints)     
# print(type(ints))





     
