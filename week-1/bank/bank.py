greetings = ("Hello", "hello,", "Hello,","hello")
user = input("Greeting: ").strip(" ")
name_user = user.split()
greeting = name_user[0]


match greeting:
    case "Hello" | "Hello," | "hello" | "hello,":
        print("$0")
if greeting not in greetings:
    match greeting[0]:
        case "H" | "h":
            print("$20")
        case _:
            print("$100")




