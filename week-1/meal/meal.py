def main():
    time = input("What time is it? ")
    convert(time)
    decimal_hours = convert(time)

    if 7.0 <= decimal_hours < 12.0:
        print("Breakfast time")
    elif 12.0 <= decimal_hours < 15.0:
        print("Lunch time")
    elif 18.0 <= decimal_hours < 21.0:
        print("Dinner time")

def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60

if __name__ == "__main__":
    main()

