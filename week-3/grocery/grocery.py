grocery = {}

while True:
    try:
        item = input()
        item = item.upper()
    
    except EOFError:
        print()
        break
    
    if item.upper() in grocery:
        grocery[item] += 1
    else:
        grocery[item.upper()] = 1

for item in sorted(grocery.keys()):
    print(grocery[item], item)


#Allow user to fill in a list of items, one per line, until control d is pressed
# Take the items add them to a list.
# Return a list where the items are sorted, upppercase and it
# Shows the quantity of each item