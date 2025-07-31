def main():
    user = input("")
    print(convert(user))

def convert(user):
    if ":)" or ":(" in user:
        user = user.replace(":)", "🙂")
        user = user.replace(":(", "🙁")

    return user






if __name__ == "__main__":
    main()



