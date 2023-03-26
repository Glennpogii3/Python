print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")


greeting = "Hello"
name = "Glenn Tolentino"
print(greeting + name)

# if we want a space, we can add that too
print(greeting + ' ' + name) # Concatenate the return string


age = 24
print(age)

print(str(greeting))
print(int(age))

age_in_words = "2 years"
print(name + " is " , age , " years old ")
print(int(age))


age_in_words = "2 years"
print(name + f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")