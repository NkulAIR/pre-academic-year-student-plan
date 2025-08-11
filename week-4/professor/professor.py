import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
#Prompt user for a number between 1-3 and reprompt if the input is invalid
    while True:
        level = input("Level: ")
        if level.isdigit() == True:
            if 1 <= int(level) <= 3:
                return int(level)


def generate_integer(level):
# Generates random sums structured as X+Y if level is 1 digit and XX + YY if level is 2
    score = 0
    numbers = []
    for i in range(10):
        match level:
            case 1:
                a = random.randint(0,9)
                b = random.randint(0,9)
                # numbers.append(a)
                # numbers.append(b)
            case 2:
                a = random.randint(10,99)
                b = random.randint(10,99)
            case 3:
                a = random.randint(100,999)
                b = random.randint(100,999)
            case _:
                raise ValueError

        tries = 0
        while tries < 3:
            try:
                print(f"{a} + {b} = ", end="")
                answer = int(input())
                if a + b == answer:
                    score += 1
                    break
                elif answer != a + b and tries < 2:
                    print("EEE")
                    tries += 1
                else:
                    print("EEE")
                    print(f"{a} + {b} = {a + b}")
                    break

            except ValueError:
                tries += 1
                print("EEE")
        else:
            print(f"{a} + {b} = {a + b}")
            break

    print("Score: ",score)
    # print(numbers)



if __name__ == "__main__":
    main()

