import sys

try:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".py"):
        # file = sys.argv[1]
        try:
            with open(sys.argv[1]) as file:
                lines = file.readlines()
                # count = 0
                # for line in file:
                #     if line.startswith("#") or not line:
                #         pass
                #     else:
                #         count += 1
            print(lines)

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")
except IndexError:
    sys.exit("Too few command-line arguments")

# count = 0

# if len(sys.argv) > 1:
#     sys.exit("Too many command-line arguments")
# if len(sys.argv) <= 0:
#     sys.exit("Too few command-line arguments")
# else:
#     if sys.argv[0]:
#         with open(sys.argv[0]) as file:
#             for line in file:
#                 if line.startswith("#") or not line:
#                     pass
#                 else:
#                     count += 1
#         print(count)
#     else:
#         sys.exit("File does not exist")