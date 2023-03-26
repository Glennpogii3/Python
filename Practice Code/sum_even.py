def sum_eo(n, t):
    
    if t == "e":
        start = 2 
    elif t  == "o":
        start = 1 
    else: 
        return -1
        
    return sum(range(start, n, 2))


x = sum_eo(11, 'spam')
print(x)


quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.

for char in quote: 
    if char.isupper():
        print(char, end="")
