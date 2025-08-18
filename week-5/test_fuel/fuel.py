def main():
    print(convert("1/2"))


def convert(fraction):
    if "/" in fraction:
        if fraction[0].isdigit():
            if fraction[-1].isdigit():
                try:
                    x, y = int(fraction[0]), int(fraction[-1])
                    return(x,y)
                except ValueError("Not an integer")
                



def gauge(percentage):
    ...


if __name__ == "__main__":
    main()