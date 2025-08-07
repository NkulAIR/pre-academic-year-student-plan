months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September" : 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    try:
        user = str(input("Date: ")).strip(" ")
        if "," not in user and "/" not in user:
            continue
        user = user.split(" ")
        if user[0] in months:
            month = user[0]
            n_month = months[month]
            day = int(user[1].strip(","))
            year = user[2]
            
            if n_month <= 12 and day <= 31:
                print(f"{year}-{n_month:02}-{day:02}")
                break

        elif user[0].isdigit:
            user = str(*user)
            user = user.split("/")
            if user[0] in months:
                continue
            month, day, year = int(user[0]), int(user[1]), int(user[2])
            if month <= 12 and day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break

    except TypeError:
        pass
    
    except ValueError:
        month, day, year = user[0],  int(user[1]), int(user[2])
        n_month = months[month]
        if int(day) <= 31:
            print(f"{year}-{n_month:02}-{day:02}")
            break



#Turn user input to string and split year, day and month it with empty space
#If month is not a int it raise ValueError, do the same process of splitting the string to find the month
# Create a numbered list
# If userdate month is in months, numbered list. return that month or its count only
# Create a boolean variable to break out of the While loop