def main():
    while True:
        try:
            fraction = input("Fraction: ")
            if "/" in fraction and fraction.count("/") == 1:
                percentage = int(convert(fraction))
                # print(convert(fraction))
                print(gauge(percentage))
                break

        # except ValueError:
        #     continue
        except TypeError:
            continue



def convert(fraction):
    fraction = fraction.split("/")
    x,y = int(fraction[0]), int(fraction[1])
    if x < 0 or y < 0:
        raise ValueError("Negative")

    if x <= y:
        percentage = int(round((x / y) * 100))
        return percentage


    # else:

    #     elif y == 0:
    #         raise ZeroDivisionError

    #     elif x and y != int() or x > y:
    #         raise ValueError



def gauge(percentage):

    try:
        percentage = int(percentage)
    except TypeError:
        raise ValueError
    else:
        if percentage == int(percentage):
            if percentage >= 99:
                return "F"

            elif percentage <= 1:
                return "E"
            else:
                return f"{percentage}%"
        else:
            raise ValueError


if __name__ == "__main__":
    main()

