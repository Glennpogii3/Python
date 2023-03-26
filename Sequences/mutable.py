computer_parts = ["Cpu", 
                  "monitor", 
                  "mouse", 
                  "keyboard", 
                  "mouse mat",
                  "headset"
                  ]


another_parts = computer_parts 
print(id(another_parts))
print(id(computer_parts))

computer_parts +=  ["Speaker"] # Mutable list
print(computer_parts) #Mutated list 
remove_parts = computer_parts.remove('headset')
print(computer_parts)

a = b = c = d = e = f = g = h = i = j = k = another_parts # Binding multiple name into list

