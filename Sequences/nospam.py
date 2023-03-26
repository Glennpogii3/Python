menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
# Solution 1 for removing the spam in list
# for meal in menu: 
#     for index in range(len(meal)- 1, -1, -1):    
#         if meal[index] == "spam":  
#             del meal[index]
#         else: 
#             pass
    
#     print(meal)


#Solution 2 in for removing the spam in the list
for meal in menu: 
    for item in meal: 
        if item != "spam":
            print(item)
    print()