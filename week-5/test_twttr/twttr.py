def main():
    word = input("Input: ")
    print(shorten(word))



def shorten(word):

        while any(char.lower() in "aeiou" for char in word):
            new_string = ""
            for char in word:
                if char.lower() not in "aeiou":
                    new_string += char
            word = new_string

        else:
             return word


if __name__ == "__main__":
    main()


