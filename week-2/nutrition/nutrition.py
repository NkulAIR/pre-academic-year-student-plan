
fruits = {"apple" : 130,
        "avocado" : 50,
        "banana" : 110,
        "cantaloupe" : 50,
        "grapefruit" : 60,
        "grapes" : 90,
        "honeydew Melon" : 50,
        "kiwifruit" : 90,
        "lemon" : 15,
        "lime" : 20,
        "nectarine" : 60,
        "orange" : 80,
        "peach" : 60,
        "pear" : 100,
        "pineapple" : 50,
        "plums" : 70,
        "strawberries" : 50,
        "sweet cherries" : 100,
        "tangerine" : 50,
        "watermelon" : 80,
        }

fruit = input("Item: ").strip(" ")
fruit = fruit.lower()

if fruit in fruits:
    print("Calories:", fruits[fruit])
else:
    pass






# match fruit:
#     case "apple":
#         print(f"Calories: {fruit["Apple"]}")
#     case "banana":
#         print(f"Calories: {fruit["Banana"]}")
#     case "avocado":
#         print(f"Calories: {fruit["Avocado"]}")
#     case "cantaloupe":
#         print(f"Calories: {fruit["Cantaloupe"]}")
#     case "grape fruit":
#         print(f"Calories: {fruit["Grapefruit"]}")
#     case "grapes":
#         print(f"Calories: {fruit["Grapes"]}")
#     case "honeydew melon":
#         print(f"Calories: {fruit["Honeydew Melon"]}")
#     case "kiwifruit":
#         print(f"Calories: {fruit["Kiwifruit"]}")
#     case "lemon":
#         print(f"Calories: {fruit["Lemon"]}")
#     case "lime":
#         print(f"Calories: {fruit["Lime"]}")
#     case "nectarine":
#         print(f"Calories: {fruit["Nectarine"]}")
#     case "orange":
#         print(f"Calories: {fruit["Orange"]}")
#     case "peach":
#         print(f"Calories: {fruit["Peach"]}")
#     case "pear":
#         print(f"Calories: {fruit["Pear"]}")
#     case "pineapple":
#         print(f"Calories: {fruit["Pineapple"]}")
#     case "plums":
#         print(f"Calories: {fruit["Plums"]}")
#     case "strawberries":
#         print(f"Calories: {fruit["Strawberries"]}")
#     case "sweet cherries":
#         print(f"Calories: {fruit["Sweet Cherries"]}")
#     case "tangerine":
#         print(f"Calories: {fruit["Tangerine"]}")
#     case "watermelon":
#         print(f"Calories: {fruit["Watermelon"]}")
#     case _:
#         pass
