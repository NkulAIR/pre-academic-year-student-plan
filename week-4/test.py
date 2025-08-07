import sys

try:
    message = "hello, my name is "
    name = sys.argv[1]
except IndexError:
    name = "user"

print(message + name)