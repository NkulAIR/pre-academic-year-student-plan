def main():
    user = input("camelCase: ").strip(" ")
    snakecase(user)
    print(f"snake_case:", snakecase(user))


    #Check if there is uppercase and split at the first occurence of uppercase
    #Convert to lowercase, split the two words and connect them with "-"
    # words = user.split()
    # contains_uppercase = [word for word in words if word[0].isupper()]
    # # uppercase = [word for word in words if word[0].isupper()]
def snakecase(user):
    snake_case = "_".join(extract_words(user))
    return snake_case.lower()

def extract_words(user):
    words = []
    current_word = ""
    for char in user:
        if char.isupper() and current_word:
            words.append(current_word)
            current_word = char
        else:
            current_word += char
    if current_word:
        words.append(current_word)
    return words

if __name__ == "__main__":
    main()

