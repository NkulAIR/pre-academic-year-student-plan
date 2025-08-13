import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

if sys.argv[1]:
    try:
        value = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=65229a318dfa8d8dc663090caae1a03bbefc26335c38d91ed9723e4cb5551c32")
    # print(json.dumps(response.json(), indent=2))
    index = response.json() #Turns it into json format so we can extract info from dictionary
    price = index["data"]["priceUsd"]

    #Edit price so it is displayed in correct format
    price = price.replace(",", "")
    cost = float(price) * float(value)
    print(f"${cost:,.4f}")



#Validate the user input. In the case where there isn't any
# If the input cannot be converted into a float(meaning it is not a number)
# Query/ get the price index, store it and access the needed data
# Reformat the data and print it as a float with 4 decimal places and commas as a seperator