import sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
else:
    file_name = sys.argv[1]
    try:
        with open(file_name) as csvfile:
            #Write a new file
    except FileNotFoundError:
        sys.exit(f"Could not read {file_name}")

            
