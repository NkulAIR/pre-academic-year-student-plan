import random
import sys

def main():
    score = 0
    tries = 0

    level = get_level()
    for i in range(10):
        a = generate_integer(level)
        b = generate_integer(level)

        while tries < 3:
            try:
                print(f"{a} + {b} =", end=" ")
                answer = int(input())
                if answer == a + b:
                    score += 1
                    break
                else:
                    tries += 1
                    print("EEE")
                    continue


            except ValueError:
                print("EEE")
                continue
        else:
            print(f"{a} + {b} = {a + b}")
            tries = 0
    print("Score: ", score)
    sys.exit()


def get_level():
#Prompt user for a number between 1-3 and reprompt if the input is invalid
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1 and level <= 3:
                return level
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):
    match level:
        case 1:
            a = random.randint(0,9)
        case 2:
            a = random.randint(10,99)
        case 3:
            a = random.randint(100,999)
        case _:
            raise ValueError

    return a


if __name__ == "__main__":
    main()



