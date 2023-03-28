# jabber = open('Jabberwocky.txt', 'r')

# for line in jabber:
#     print(line.rstrip())
#     # print(len(line))

# jabber.close()

# with open(r'C:\xampp\htdocs\Python\TextFiles\Jabberwocky.txt', 'r') as jabber: 
#     # for line in jabber:
#     #     print(line.rstrip())
#     lines = jabber.readlines()

# print(lines)
# print(lines[-1:]) 
# for line in reversed(lines):
#     print(line, end='')


# with open(r'C:\xampp\htdocs\Python\TextFiles\Jabberwocky.txt', 'r') as jabber:
#     text = jabber.read()
# print(text)

# for char in reversed(text):
#     print(char, end='')

# with open(r'C:\xampp\htdocs\Python\TextFiles\Jabberwocky.txt', 'r') as jabber:
#     while True:
#         line = jabber.readline().rstrip()
#         print(line)
#         if 'jubjub' in line.casefold():
#             break 
        
# print('*' * 80)

with open(r'C:\xampp\htdocs\Python\TextFiles\Jabberwocky.txt', encoding='utf-8') as jabber: 
    for line in jabber:
        print(line.rstrip())
        # if 'jubjub' in line.casefold():
        #     break 
 


