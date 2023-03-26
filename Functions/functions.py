def multiply(x, y):
    """
    
        
    :param multipy: 
    :return:
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    
    """
    
    :param is_palindrome: 
    :return:
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1] == string

def palindrome_sentence(sentence):
    """
    
    :param palindrome_sentence: 
    :return:
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


def fibonacci(x, y):
    for f in range(1, 10): 
        if f > 2: 
            pass

            

def divide(a, b):  
    result = a // b
    return result

            

word = input("Please enter a word to check:")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else: 
    print("'{}' is not a palindrome".format(word))


# word = input("Please enter a word to check: ")
# if palindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()

for val in range(1, 10):
    two_times = multiply(2, val)
    print(two_times)





sagot = divide(10, 2)
print(sagot)


p = is_palindrome()