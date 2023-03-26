available_exits = ["north", "east", "south", "west"]

chosen_exit = ""
while chosen_exit not in available_exits: 
    chosen_exit = input("Enter ur preffered exit: ")
    if  chosen_exit.casefold() == "quit": 
        print ("Game over")
        break
    

else:
    print("aren't you glad you got out of there")
