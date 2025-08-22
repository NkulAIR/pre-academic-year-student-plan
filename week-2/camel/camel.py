def main():
    word = ""
    user = input("camelCase: ").strip(" ")
    for i in user:
        if i.isupper():
            word += "_"
            word += str(i).lower()
        else:
            word += i
    print("snake_case:",word)



if __name__ == "__main__":
    main()
# Iterate through word if current char is capital letter add, "_"
# Otherwise add current char