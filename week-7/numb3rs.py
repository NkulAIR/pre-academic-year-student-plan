import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^.+\..+\..+\..+\$", ip):
        return True
    return False




if __name__ == "__main__":
    main()