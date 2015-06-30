print("Welcome to Mailroom Madness")


def thankyou():
    # thank you


def report():
    # report


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
        print("Please select one of the options above.")
