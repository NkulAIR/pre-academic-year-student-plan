import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
else:
    file_name = sys.argv[1]
    try:
        file_name1 = file_name
        file_name2 = sys.argv[2]

        with open(file_name1) as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
        
        if sys.argv[2].endswith(".csv"):
            with open(file_name2, "w") as file:
                f_names = ["first", "last", "house"]
                writer = csv.DictWriter(file, fieldnames= f_names)
                writer.writeheader()

                for info in data:
                    name = info["name"] 
                    house = info["house"] 

                    last, first = name.split(", ")
                    writer.writerow({"first": first.strip(), "last": last.strip(), "house": house})
        else:
            sys.exit("Invalid file name") 

    except FileNotFoundError:
        sys.exit(f"Could not read {file_name}")

            
