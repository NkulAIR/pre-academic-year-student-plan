def main():
    fuel = input("")
    percent = convert(fuel)
    print(gauge(percent))


def convert(fraction):
    if "/" in fraction:
        if fraction[0].isdigit():
            if fraction[-1].isdigit():
                if fraction[0] > fraction[-1]:
                    raise ValueError("")
                elif fraction[-1] == 0:
                    raise ZeroDivisionError("")
                else:
                    x, y = int(fraction[0]), int(fraction[-1])
                    p = round((x / y) * 100)
                    return p
                
            raise ZeroDivisionError("Y")
        raise ValueError("X")


def gauge(percentage):
    if int(percentage) <= 1:
        return "E"
    if int(percentage) >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()