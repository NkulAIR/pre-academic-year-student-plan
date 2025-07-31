answer = ["forty-two", "forty two", "42"]
user = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
user_answer = user.strip(" ").lower()

if user_answer in answer:
    print("Yes")
elif user_answer == "FORTY-TWO":
    print("Yes")
elif user_answer == "FORTY TWO":
    print("Yes")
else:
    print("No")
