available_parts = ["Speaker", 
                  "CPU", 
                  "Mouse", 
                  "Keyboard", 
                  "Headset",
                  "HDMI"
                  ]

#valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1): 
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = [] #Empty list of computer parts

while current_choice != '0': 
    if current_choice in valid_choices: 
        index = int(current_choice) - 1
        chosen_parts = available_parts[index]
        if chosen_parts in computer_parts:
            print("Removing {}".format(current_choice))  
            computer_parts.remove(chosen_parts)
        else: 
            print("Adding {}".format(current_choice)) 
            computer_parts.append(chosen_parts)
        print("Your list contains {}".format(computer_parts)) 
    else:  
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):  # for part it means taking the available parts in the list. For loop
            print("{0}: {1}".format(number + 1, part)) # is used to add numbering in the list
    
    current_choice = input()
    
print(computer_parts)

