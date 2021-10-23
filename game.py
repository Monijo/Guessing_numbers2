def users_inputs():
    print("If your number is bigger print: bigger, if is lower print:lower and if I guess: you win ")
    list_of_possibilities = ['bigger', 'lower', 'you win']
    users_answer = input()
    while users_answer not in list_of_possibilities:
        print("Don't cheat me!")
        users_answer= input()
    return users_answer


def guessing_number():
    print("Let's play!Imagine  number in the range 0-1000 and I will guess your number in max 10 attempts!")
    print(input("If you have one please press 'Enter' to continue!"))


    min = 0
    max = 1000
    while True:
        guess = int((max - min) / 2) + min
        print(f"I guess: {guess}")
        user_answer = users_inputs()
        if user_answer == "lower":
            max = guess
        elif user_answer == "bigger":
            min = guess
        else:
            print("I win!")
            break



guessing_number()