def main():
    try:
        user = input("Greeting: ").strip(" ").lower()
        name_user = user.split()
        greeting = name_user[0]
        print(f"${value(greeting)}")

    except IndexError:
        print(f"${100}")



def value(greeting):

    match greeting:
        case "Hello" | "Hello," | "hello" | "hello,":
            return int(0)

    if greeting != "Hello" or "hello":
        match greeting[0]:
            case "H" | "h":
                return int(20)
            case _:
                return int(100)


if __name__ == "__main__":
    main()