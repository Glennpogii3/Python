low = 1  
high = 1000 

print("Please think a number from {} to {}".format(low, high))
input("Please enter to start")

guesses = 1 

while low != high: 
    # print("\tGuessing a number from {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should i guess higher or lower ?"
                     "Enter h or l, or c if my guess was correct "
                     .format(guess)).casefold()
    
    if high_low == "h":
            #
        low = guess + 1 
    elif high_low == "l":
            #
        high = guess - 1
    elif high_low == "c":
        print("i got it in {} guesses!".format(guesses))
        break 
    else:
        print("Please select h, l or c")
        
    # guesses = guesses  + 1  Longhand
    guesses += 1 
    
else: 
    print("You thougt of the number {}".format(low))
    print("I got it in {} guesses!".format(guesses))
    