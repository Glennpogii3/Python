# i = 0

while i < 10:
    print("i is now {}".format(i))
    i += 2     # the result is counting by 3. 
    i = i + 2  #
    
    
# for i in range(0, 100, 7):
#     print(i)
#     if i > 0 and i % 11 == 0:
#      break


# for i in range(21):
#     if i % 3 == 0 or i % 5 == 0:
#         continue 
#     print(i)
    
# # without continue
# for x in range(21):
#     if x % 3 != 0 and x % 5 != 0:
#         print(x)
    
    
# number = int(input('Enter any number between 100 and 500 '))
# # number greater than 100 and less than 500
# while number < 100 or number > 500:
#     print('Incorrect number, Please enter correct number:')
#     number = int(input('Enter a Number between 100 and 500 '))
# else:
#     print("Given Number is correct", number)



# name = 'Jesaa29Roy'
# size = len(name)
# i = 0
# # iterate loop till the last character
# while i < size:
#     # break loop if current character is number
#     if name[i].isdecimal():
#         break;
#     # print current character
#     print(name[i], end=' ')
#     i = i + 1