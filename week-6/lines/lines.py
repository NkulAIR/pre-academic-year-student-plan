import sys

try:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".py"):
        try:
            count = 0
            with open(sys.argv[1]) as file:
                for line in file:
                    if not line.lstrip().startswith("#") and line.lstrip() != '':
                        count += 1
                    else:
                        pass
            print(count)
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")
except IndexError:
    sys.exit("Too few command-line arguments")


#Check if sys.argv[1] is there if not dont run program
#Open the target file and read how many lines are in it
#Count only lines of code
#Print the number of lines


#Not count comments