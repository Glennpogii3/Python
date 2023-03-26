#                   1
#         012345678901234
parrot = "Norwegian Blue"

print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw
print(parrot[0:5:9])    # N

# Exercise str Data type String



number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])



str1 = 'uvghizefjkwylanopqrbcdmst'

values = ''.join(sorted(str1))
print(values)
