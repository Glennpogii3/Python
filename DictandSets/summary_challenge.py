choice = "-"
while choice != "0":   # is not zero  if equals to 0 then quit 
    if choice in set("12345"):                   #if you choose 1 to 5 
        print("You chose {}".format(choice)) # Print this with number of choice 
    else:   # else if you did not choose the 1 to 5 and perform this method.
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")
    
    choice = input() # Input function 