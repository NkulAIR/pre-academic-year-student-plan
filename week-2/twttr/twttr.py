input_string = input("Input: ")
while any(char.lower() in "aeiou" for char in input_string):
    new_string = ""
    for char in input_string:
        if char.lower() not in "aeiou":
            new_string += char
    input_string = new_string

print("Output:", input_string)


#1 While there is a character which is in the vowels, in the input string keep running. If this is not the case, skip the process & return the user input as it is
#2. new string to accumalate non-vowels
#3. Iterate through the input string and if the current letter(case insensitive) is not in the vowels.
#4. Increment the character to new string.
#5. Convert user input to new string and print it









