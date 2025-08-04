while True:
    try:
        print("Please enter a proper fraction or press Ctrl + C to exit program")
        user_input = input("Fraction: ")
        user_input = user_input.split("/")
        x, y = int(user_input[0]), int(user_input[1])
        if x < 0 or y < 0:
            continue


    except ValueError:
        pass

    except ZeroDivisionError:
        # print("0")
        pass

    except KeyboardInterrupt:
        print("\nProgram Exitted Succesfully")
        break
    
    else:
        if x <= y:
            fraction = round((x / y) * 100)
            if fraction >= 99:
                print("F")
            elif fraction <= 1:
                print("E")
            else:
                print(f"{fraction}%")
            break
            
    
