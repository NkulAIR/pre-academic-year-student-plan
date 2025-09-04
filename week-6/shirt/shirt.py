import sys
import sys
from PIL import Image, ImageOps

def main():
    if validate():
        apply_shirt()

def validate():
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
                return input_file, output_file
        except FileNotFoundError:
            sys.exit(f"Could not read{file_name}")

def apply_shirt():
    img1, img2 = validate()[0], validate()[1]
    images = []

    try:
        with Image.open("shirt.png") as shirt:
            size = shirt.size

            try:
                with Image.open(img1) as before:
                    img_size = before.size
                    muppet = ImageOps.fit(before, size=(600,600))
                    pic_size = (600, 600)
                    images.append(muppet)
                    print(images)

            except FileNotFoundError:
                sys.exit(f"{sys.argv[1]} not found")

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()