def main():
    paid = []
    amount_due = 50

    while sum(paid) != 50:
        if amount_due < 0:
            print("Amount Due: ", 0)
        else:
            print("Amount Due:", abs(amount_due))
        payment = int(input("Insert Coin: "))

        if valid_coins(payment):
            paid.append(payment)
            amount_due -= payment
        else:
             print("Amount Due:", 50)

        if sum(paid) > 50:
            print("Change Owed:", (sum(paid) - 50))
            break

    else:
        print("Change Owed:", (sum(paid) - 50))



def valid_coins(payment):
    match payment:
        case 5 | 10 | 25:
            return payment
        case 50:
            return payment
        case _:
            pass


if __name__ == "__main__":
    main()
