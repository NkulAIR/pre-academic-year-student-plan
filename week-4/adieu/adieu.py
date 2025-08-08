import inflect
p = inflect.engine()

# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa
# Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
# Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl


names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)

    except EOFError:
        print()
        break


output = p.join(names)
print("Adieu, adieu, to " + output)

# if len(names) == 1:
#   print("Adieu, adieu, to ", *names)

# elif len(names) == 2:
#   print(f"Adieu, adieu, to {names[0]} and {names[1]}")



# else:
#     farewell = ", ".join(names[:-1])
#     last_name = names[-1]
#     print(f"Adieu, adieu, to {farewell} and {last_name}")



# Take all the names and put them into a single list
# Slice the last two names and join them with an "and"
# Seperate names in the list with a comma
# Output a formatted string