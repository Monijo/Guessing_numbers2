def users_inputs():
    """ Return proper value provided by user
        :rtype: str
    """
    print("If your number is bigger print: bigger, if is lower print:lower and if I guessed: you won ")
    list_of_possibilities = ['bigger', 'lower', 'you won']
    users_answer = input().lower()
    while users_answer not in list_of_possibilities:
        print("Don't cheat me!")
        users_answer= input().lower()
    return users_answer


def guessing_number():
    """Main function for our program"""
    print("Let's play!Imagine  number in the range 0-1000 and I will guess your number in max 10 attempts!")
    print(input("If you have one please press 'Enter' to continue!"))
    min = 0
    max = 1000
    hits = 0
    while True:
        guess = int((max - min) / 2) + min
        print(f"I guess: {guess}")
        hits += 1
        user_answer = users_inputs()
        if user_answer == "lower":
            max = guess
        elif user_answer == "bigger":
            min = guess
        else:
            print(f"I won!!!I guessed in {hits} times!")
            break

if __name__ == "__main__":
    guessing_number()