import sys
import pyfiglet
import random

fonts = pyfiglet.FigletFont.getFonts()

try:
    if len(sys.argv) >= 3 and sys.argv[2] in fonts:
        if sys.argv[1] == "--font" or sys.argv[1] == "-f":
            text = input("Input: ")
            font = sys.argv[2]

            custom_fig = pyfiglet.Figlet(font=sys.argv[2])
            ascii_art = custom_fig.renderText(text)
            print("Output: ")
            print(ascii_art)
        else:
             print("Invalid usage")
             sys.exit(1)
    
    elif len(sys.argv) == 1:
        text = input("Input: ")
        #  fonts = pyfiglet.FigletFont.getFonts()
        random_font = random.choice(fonts)
        custom_fig = pyfiglet.Figlet(font=random_font)
        ascii_art = custom_fig.renderText(text)
        print("Output: ")
        print(ascii_art)

    else:
        print("Invalid usage")
        sys.exit(1)


except pyfiglet.FontNotFound:
    print("Invalid Usage")
    sys.exit(1)

except IndexError:
    print("Invalid Usage")
    sys.exit(1)