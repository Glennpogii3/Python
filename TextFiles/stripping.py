# filename = (__filename_Path) # not working directory 

with open(r'C:\xampp\htdocs\Python\TextFiles\Jabberwocky.txt', 'r')  as poem:
    first = poem.readline().strip()

def removeprefix(string: str, prefix: str, /) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]
    
def removesuffix(string: str, suffix: str, /) -> str:
    # suffix='' should not call self[:-0].
    if suffix and string.endswith(suffix):
        return string[:-len(suffix)]
    else:
        return string[:]
    


print(first)

chars = "'Twas be wonasd "
# no_apostrophe = first.strip(chars)
# print(no_apostrophe)

for character in first: 
    if character in chars:
        print(f'removing"{character}"')
    else: 
        break
    
print("*" * 80)

for character in first[::-1]: # process backwards 
   if character in chars:
        print(f'removing"{character}"')
   else: 
        break
 
print("*" * 80)

#twas_removed = first.removeprefix("'Twas")
twas_removed = removeprefix(first, "'Twas")
print(twas_removed)

toves_removed = removesuffix(first, 'toves')
#toves_removed = first.removesuffix('toves')
print(toves_removed) 
        


    