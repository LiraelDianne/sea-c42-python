import sys

donors = {"Bill Gates": [200, 600, 300], "Elon Musk": [500, 400],
          "Your Mom": [5, 20], "Harry Potter": [38.24],
          "Tony Stark": [500, 500, 500]}

print("Welcome to Mailroom Madness")


def menu():
    options = {"t": thankyou, "r": report, "w":all_thank_yous, "quit": sys.exit}
    print("Choose from the following:")
    print("T - Send a (T)hank You")
    print("R - Create a (R)eport")
    print("W - write a Thank You to everyone")
    print("quit - Quit the program")
    choice = input()
    choice = choice.lower()
    if choice in options:
        options[choice]()
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
    new_donation = formatNum(float(donationAmount(donor_name)))
    donors[donor_name].append(new_donation)
    thankyouMessage = make_thankyou(donor_name, new_donation)
    print(thankyouMessage)
    print(input("Press Enter to Continue..."))
    menu()


def make_thankyou(name, donation):
    message = ("Dear {}, \n Thank you so much for your kind donation of {}. We"
               " here at the Foundation for Homeless Whales greatly appreciate"
               " it. Your money will go towards creating new oceans on the "
               "moon for whales to live in.\n Thanks again, \n Crystal "
               "Stellwagen \n Director E. H. W.").format(name, donation)
    return message


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
    total = total_donations(donor)
    name = donor
    number = len(donors[name])
    avg = formatNum(total/number)
    total = formatNum(total)
    line = "%s \t| %s \t| %s \t| %s" % (name, total, number, avg)
    return line


def total_donations(donor):
    total = 0.0
    for num in range(len(donors[donor])):
        total = total + donors[donor][num]
    return total


def formatNum(number):
    # format a dollar amount so it will appear as $nn.nn
    num = round(number, 2)
    if (num * 10) % 1 == 0:
        num = str(num) + "0"
    num = "$" + str(num)
    return num


def all_thank_yous():
    for donor in donors:
        name = "_".join(donor.split(" "))
        thankyou_file = open(name, 'w')
        message = make_thankyou(donor,  formatNum(total_donations(donor)))
        thankyou_file.write(message)
        menu()


if __name__ == "__main__":
    menu()
