items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

cart = []
print("Welcome to Felipe's taqueria🌞 Please pick an item from our menu")
while True:
    try:
        order = input("Item: ").strip(" ")
        order = order.title()

        if order in items:
            item = (items[order])
            cart.append(item)
            total = sum(cart)
            print(f"Total: ${total:.2f}")

    except KeyboardInterrupt:
        print("Visit us again soon🌞")
        break

    except EOFError:
        print("Ctrl + D pressed. Exiting menu......")
        print("🌞Enjoy your meal🌞")
        break


#Take the customers order. One item per line if it's an invalid item reprompt
# Get the food item from the list add it to the cart
# Give the customer the sum of all items in the cart and allow them end to the order



