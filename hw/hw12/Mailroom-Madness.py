import sys

donors = {"Bill Gates": [200, 600, 300], "Elon Musk": [500, 400],
          "Your Mom": [5, 20], "Harry Potter": [38.24],
          "Tony Stark": [500, 500, 500]}

print("Welcome to Mailroom Madness")


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


def thankyou():
    # Generate a thank you message
    print("Please enter a name, or choose from the following:")
    print("list - Print a list of previous donors")
    print("back - Return to main menu")
    donor_name = choosename()
    if donor_name not in donors:
        donors[donor_name] = []
    new_donation = float(donationAmount(donor_name))
    donors[donor_name].append(new_donation)
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
    # allow user to input a donor name or choose from the list
    choice = input()
    if choice == 'back':
        menu()
    elif choice == 'list':
        for donor in donors:
            print(donor)
        print("Please type a name from the list, or enter a new donor name.")
        choice = choosename()
        return choice
    else:
        return choice


def donationAmount(donor):
    # input a donation amount and verify that it is a number
    print("Please enter a donation amount.")
    print("back - Return to main menu")
    choice = input()
    if choice == 'back':
        if donor in donors:
            del donors[donor]
        menu()
    elif not is_number(choice):
        print("Please make sure your donation amount is a number.")
        choice = donationAmount(donor)
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
    # generate a report of all donors
    print("Name \t\t| Total \t| # \t| Average")
    for donor in donors:
        print(makeline(donor))
    menu()


def makeline(donor):
    # format a line for a single donor and related info
    total = 0.0
    name = donor
    number = len(donors[name])
    for num in range(len(donors[name])):
        total = total + donors[name][num]
    avg = formatNum(total/number)
    total = formatNum(total)
    line = "%s \t| %s \t| %s \t| %s" % (name, total, number, avg)
    return line


def formatNum(number):
    # format a dollar amount so it will appear as $nn.nn
    num = round(number, 2)
    if (num * 10) % 1 == 0:
        num = str(num) + "0"
    num = "$" + str(num)
    return num

if __name__ == "__main__":
    menu()
