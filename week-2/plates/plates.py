def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(string):
    if len(string) <= 6 and len(string) >= 2:
        if string.isalpha():
            return True
        if " " in string or "." in string:
            return False
        else:
            for char in string:
                if char in "%$@!,:?-;')_/.&(^\"":
                    return False
                if char.isdigit():
                    if string[-2].isdigit() and string[0].isalpha():
                        n_string = string[len(string.rstrip("0123456789")):]
                        if n_string.isdigit():
                            if n_string[0] == "0":
                                return False
                            else:
                                pass
                            return True
                        else:
                            return False
                    else:
                        return False

    return False


main()

# If length of string is longer than / equal to 2 char or shorter than or equal 6 chars
# If the string has digits only the last part can be digits and the first part of the string must be a letter
# If the string has punctuation marks, it is invalid
# If the string has "." it is invalid
# If the first number used on the plate is 0, it is invalid




