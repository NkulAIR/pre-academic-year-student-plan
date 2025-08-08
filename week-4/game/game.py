import random
import sys



while True:
    n = input("Level: ")
    if n.isdigit() and int(n) > 0:
        number = random.randint(1,int(n))

    else:
        print("Invalid level")
        continue


    while n.isdigit():
        guess = input("Guess: ")
        if guess.isdigit():
            guess = int(guess)
            if guess == number:
                print("Just right!")
                sys.exit(0)

            elif guess > number:
                print("Too large!")
                continue

            elif guess < number:
                print("Too small!")
                continue

        else:
            print("Invalid guess")
            continue

# Prompt user for a level, validate the input make sure it is a postive integer
# Generate random number between 1 and range
# Allow the user to guess the number.Reprompt if it's invalid
# Tell them if their guess is too low, too high or correct(Just right)









