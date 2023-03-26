def fizz_buzz(guess: int) -> str:
    
        if guess % 15 == 0:
            return "fizz buzz"
        elif guess % 3 == 0:
            return "fizz"
        elif guess % 5 == 0:
            return "buzz"
        else:
            return str(guess)


input("Play Fizz buzz.  Press Enter to start")
print()

next_number = 0 


while next_number < 99: 
    next_number += 1 
    print(fizz_buzz(next_number))
    next_number = next_number + 1
    correct_answer = fizz_buzz(next_number) 
    players_answer = input("Your go: ")
    # players_answer = correct_answer
    if players_answer != correct_answer:
        print("Wrong answer, the correct answer should be {}".format(correct_answer))
        break
    else: 
        print("Correct answer {}".format(next_number))