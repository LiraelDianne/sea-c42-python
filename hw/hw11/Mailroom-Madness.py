import sys

donorList = ["Bill Gates", "Elon Musk", "Your Mom",
             "Harry Potter", "Tony Stark"]
donations = {"Bill Gates": [200, 600, 300], "Elon Musk": [500, 400],
             "Your Mom": [5, 20], "Harry Potter": [38.24],
             "Tony Stark": [500, 500, 500]}

print("Welcome to Mailroom Madness")


def thankyou():
    print("Please enter a name, or choose from the following:")
    print("list - Print a list of previous donors")
    print("quit - Return to main menu")
    donor_name = choosename()
    if donor_name not in donorList:
        donorList.append(donor_name)
        donations[donor_name] = [0]
    new_donation = float(donationAmount())
    donations[donor_name].append(new_donation)
    thankyouMessage = ("Dear %s, \n Thank you so much for your " % donor_name +
                       "kind donation of $%s0. We here at " % new_donation +
                       "the Foundation for Homeless Whales greatly " +
                       "appreciate it. Your money will go towards creating " +
                       " new oceans on the moon for whales to live in. \n " +
                       "Thanks again, \n Jim Grant \n Director E. H. W.")
    print(thankyouMessage)
    print(input("Press Enter to Continue..."))
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
    elif not is_number(choice):
        print("Please make sure your donation amount is a number.")
        choice = donationAmount()
        return choice
    else:
        return choice


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def report():
    print("Name \t\t| Total \t| # \t| Average")
    for donor in donorList:
        print(makeline(donor))
    menu()


def makeline(donor):
    total = 0.00
    name = donor
    number = len(donations[name])
    for num in range(len(donations[name])):
        total = total + donations[name][num]
    avg = format(total/number)
    total = format(total)
    line = "%s \t| $%s \t| %s \t| $%s" % (name, total, number, avg)
    return line


def format(number):
    num = round(number, 2)
    if (num * 10) % 1 == 0:
        num = str(num) + "0"
    return num


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
