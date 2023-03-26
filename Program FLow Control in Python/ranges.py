for i in range(1, 20): 
    print("i is now {}".format(i))

# This solution uses a step value for the range function
for i in range(0, 101, 7):
    print(i)


# This solution uses a slice
for i in range(101)[::7]:
    print(i)
