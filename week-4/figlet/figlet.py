import sys
import pyfiglet
import random

fonts = pyfiglet.FigletFont.getFonts()

try:
    print(sys.argv[2])
except pyfiglet.FontNotFound:
    print("Invalid Usage")
    sys.exit(1)

except IndexError:
    print("Invalid Usage")
    sys.exit(1) add figlet