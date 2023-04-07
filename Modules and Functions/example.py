import shelve

# print(dir())
# print()
# print(dir(shelve))
# #print(dir(__annotations__))
# for shelvess in dir(shelve):
#     print(shelvess)
#
# print()

for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)
