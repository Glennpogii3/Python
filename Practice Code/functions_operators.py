# def add (a, b): 
#     result = a + b
#     return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


# word = input("Please enter a word to check:")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else: 
#     print("'{}' is not a palindrome".format(word))


def palindrome_sentence(sentence):
    string = "" 
    for char in sentence: 
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)            

words = input("Please enter a word to check:")
if palindrome_sentence(words):
    print("'{}' is a palindrome".format(words))
else: 
    print("'{}' is not a palindrome".format(words))


# answer = add (12, 23)
# print(answer)

# print()
# for val in range(1, 5):
#     addition = add (10, val)
#     print(addition)
    
