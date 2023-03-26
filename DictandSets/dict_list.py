available_parts = {"1": "Speaker", 
                  "2": "CPU", 
                  "3": "Mouse", 
                  "4": "Keyboard", 
                  "5": "Headset",
                  "6": "HDMI"}

current_choice = None

computer_parts = [] #Empty list of computer parts

while current_choice != "0":
    if current_choice in available_parts: 
       chosen_parts = available_parts[current_choice]
       print(f"Adding {chosen_parts}")
       
       if chosen_parts in computer_parts:
            print("Removing {}".format(current_choice))  
            computer_parts.remove(chosen_parts)
       else: 
            print("Adding {}".format(current_choice)) 
            computer_parts.append(chosen_parts)
       print("Your list contains {}".format(computer_parts)) 
                  
    else:
       print("Please add options from the list")
       
       for key, value in available_parts.items():
           print(f"{key}: {value}")
           
       
       print("0: to quit")
       

    
    current_choice = input("> ")
    
    
    