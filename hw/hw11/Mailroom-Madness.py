import sys

donorList = ["Bill Gates", "Elon Musk", "Your Mom"]
donations = []

print("Welcome to Mailroom Madness")


def thankyou():
    print("Please enter a name, or choose from the following:")
    print("list - Print a list of previous donors")
    print("quit - Return to main menu")
    donor_name = choosename()
    if donor_name not in donorList:
        donorList.append(donor_name)
        donations[donor_name] = 0
    new_donation = donationAmount()
    donations[donor_name].append(new_donation)
    menu()


def choosename():
    choice = input()
    if choice == 'quit':
        menu()
    elif choice == 'list':
        print(donorList)
        print("Please type a name from the list, or enter a new donor name.")
        choice = choosename()
        return choice
    else:
        return choice


def donationAmount():
    choice = input("Please enter a donation amount or 'quit':")
    if choice == 'quit':
        menu()
    else:
        return choice


def report():
    print("report")
    menu()


def menu():
    print("Choose from the following:")
    print("T - Send a (T)hank You")
    print("R - Create a (R)eport")
    print("quit - Quit the program")
    choice = input()
    choice = choice.lower()
    if choice == "t":
        thankyou()
    elif choice == "r":
        report()
    elif choice == 'quit':
        sys.exit()
    else:
        print("Please select one of the options.")
        menu()
menu()
