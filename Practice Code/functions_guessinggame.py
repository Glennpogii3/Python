import random

def get_interger(prompt): 
    """
    Get an interger from standard input (stdin).
    
    The function will continue looping, and prompting
    the user, until a valid 'int' is entered.
    
    :param prompt: The string that the user will see, when 
        they're prompted to enter the value.   
    :return: The integer that user entered.
    """
    while True: 
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{0} is not a valid number".format(temp))
            
print(input.__doc__)
print("*"*80)
print(get_interger.__doc__)
print("*"*80)
highest  = 10
answer = random.randint(1, highest)
print(answer) #TODO: Remove after Testing 
guess = 0 
print("Please guess the number between 1 to {}:".format(highest))

while guess != answer:
    guess = get_interger(": ")      
    if guess == 0: 
        print ("Quit the game")
        break   
    if guess == answer:
            print("Well Done you guessed it")
            break
    else:
        if guess < answer:
            print("Please guess Higher!!")
        else:
            print("Please guess Lower!!")
            
 
    

# if guess == answer:
#     if guess < answer:
#         print("Please guess Higher!!")
#     else:
#         print("Please guess Lower!!")
#     guess = int(input())
#     if guess == answer:
#         print("May Tama ka!!")
#     else:
#         print("Pasensya Mali ang Hula mo")
# else:
#     print("Unang sagot Tama agad")
    
    
# if guess == answer:
#     print("Unang sagot Tama agad")
# else:
#     if guess < answer:
#         print("Please guess Higher!!")
#     else:
#         print("Please guess Lower!!")
#     guess = int(input())
#     if guess == answer:
#         print("May Tama ka!!")
#     else:
#         print("Pasensya Mali ang Hula mo")

# if guess < answer: 
#     print("Please guess higher")
#     guess = int(input()) 
#     if guess == answer:
#         print("Well Done Boi")
#     else:
#         print("Sorry try again")
# elif guess > answer: 
#     print("Please guess lower")
#     guess = int(input()) 
#     if guess == answer:
#         print("Well Done Boi")
#     else:
#         print("Sorry try again")
# else:
#     print("You got it right")
    
    
    
    
    
# tree1 = 'put your first tree name here'
# tree2 = 'put your second tree name here'
 
# # add the code to compare the trees
# if tree1 == tree2: 
#     print("The trees are the same")
# else:
#     print("The trees are different.")
    
    
# x = 5 
# y = 7 

# if x > y:
#     print ("x is greater than y")
# elif x < y: # Be mindful in colon.
#      print("x is smaller than y")
# else: 
#     print("x equals y")