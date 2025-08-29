import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        input_file = sys.argv[1]
        output_file = sys.argv[2]

        if input_file[-3:] != output_file[-3:]:
            sys.exit("Input and output have different extensions")
        else:
            with open(input_file) as image:
                ....
            # Include logic to write the file or place tshirt on file
        
        print(file_name[-3:])
    except FileNotFoundError:
        sys.exit(f"Could not read{file_name}")
