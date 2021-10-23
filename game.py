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
    print("If you have one please press 'Enter' to continue!")
    input()
    min = 0
    max = 1000
    user_answer = ""



users_inputs()