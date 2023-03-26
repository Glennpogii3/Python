data = [] 


# del data [0:2]
# print(data)
# del data [10:]
# print(data)

aTuple = ("Orange")
print(type(aTuple))


min_valid = 100
max_valid = 200

#process the low values in the list 
stop = 0 
for index, value in enumerate(data):
        if value >= min_valid:
                stop = index 
                break
print(stop) # for debugging 
del data[:stop]
print(data)


# process the high values in the list 

start = 0 
for index in range(len(data) - 1, -1, -1):
       if data[index] <= max_valid:
        # We have to index of the last item to keep.
        # Set 'start' ti the posistion of the first
        # item to delete, which is 1 after 'index'
           start = index + 1 
           break
   
print(start)
del data[start:] 
print(data)  

# for index, value in enumerate(data):
#         if (value < min_valid) or (value > max_valid):
#                 del data [index]
# print(data)