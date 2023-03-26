def fizz_buzz(guess: int) -> str:
    """
    Play Fizz buzz
 
    :param number: The number to check.
    :return: 'fizz' if the number is divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string, otherwise.
    """
    if guess % 15 == 0:
        return "fizz buzz"
    elif guess % 3 == 0:
        return "fizz"
    elif guess % 5 == 0:
        return "buzz"
    else:
        return str(guess)

 
for i in range(1, 101):
    print(fizz_buzz(i))
