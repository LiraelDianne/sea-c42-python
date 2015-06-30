import sys

donorlist = ["Bill Gates", "Elon Musk", "Your Mom"]

print("Welcome to Mailroom Madness")


def thankyou():
    print("Please enter a name, or choose from the following:")
    print("list - Print a list of previous donors")
    print("quit - Return to main menu")
    donor_name = choosename()
    print(donor_name)
    menu()


def choosename():
    choice = input()
    if choice == 'list':
        print(donorlist)
        print("Please type a name from the list, or enter a new donor name.")
        choice = choosename()
    elif choice == 'quit':
        menu()
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
