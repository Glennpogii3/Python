# for i in range(1, 10):
#     print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 2))
# print("*" * 80)

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18 - age))

if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age >= 120:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")


# name = input("Enter name: ")
# age = int(input("How old are you, {0}? ".format(name)))

# if age < 18:
#     print("You're a Minor, {0}".format(name))
# elif age >= 60: 
#     print("You're a Senior, {0}".format(name))
# else: 
#     print("You're a Adult, {0}".format(name))