grocery = {}

while True:
    try:
        item = input().upper()
    
    except KeyboardInterrupt:
        print()
        break

#Allow user to fill in a list of items, one per line, until control d is pressed
# Take the items add them to a list.
# Return a list where the items are sorted, upppercase and it
# Shows the quantity of each item