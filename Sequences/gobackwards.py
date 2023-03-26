data = [23, 24, 25, 26, 27, 28, 29, 30, 31, 101, 120, 121, 122, 123, 124, 125]


min_valid = 100 
max_valid = 200 
#  Removing items from the list backwards
# for index in range(len(data) -1, -1, -1):
#     if data[index] <= min_valid or data[index] >= max_valid:
#         print(index, data)
#         del data[index]
        
# print(data)
top_index = len(data) -1 
# The Reversed function
for index, value in enumerate(reversed(data)):
    if  value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]
        
print(data)
    