
# while True: 
#     shopping_list = ["milk",  "pasta", "eggs", "spam", "bread"]

#     letter = input("Enter a product")
#     if letter in shopping_list: 
#         print("{} is in {}".format(letter, shopping_list))
#         continue;
#     else:
#          print ("i dont need that letter")
#          break;
 
 


shopping_list = ["milk",  "pasta", "eggs", "spam", "bread"]

# for item in shopping_list:
#     if item != "spam":
#         print ("Buy " + item)


for item in shopping_list:
    if item == "spam":
        break;
    
    print ("Buy " + item)