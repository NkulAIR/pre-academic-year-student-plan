import sys
from tabulate import tabulate
import csv

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguements")
else:
    name, extension = sys.argv[1].split(".")
    if extension != "csv":
        sys.exit("Not a csv file")

    file_name = sys.argv[1]
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    if name == "regular":
        header = "Regular Pizza"
    header = "Sicilian Pizza"

    if data:
        headers = data[0].keys()
        table = [list(d.values()) for d in data]
        print(tabulate(table, headers=headers, tablefmt="grid"))
    

# Validate the command-line argument
# Make sure the file name exists and check for the right file extension
# Open and read the csv file
# Format the data, as ascii