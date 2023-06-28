def show_homepage():
    print("        === DonateMe Homepage ===        ")
    print("----------------------------------------")
    print("| 1.    Login    | 2.    Register       |")
    print("----------------------------------------")
    print("| 3.    Donate   | 4.  Show Donations   |")
    print("-----------------------------------------")
    print("|            5. Exit                    |")
    print("----------------------------------------")


def donate(username):
    donation_amt = float(input("\nEnter amount to donate: "))
    donation_string = f"\n{username} donated ${donation_amt}"
    print("\nThank You for donating!")
    return donation_string


def show_donations(donations):
    print("\n--- All Donations ---")
    if not donations:
        print("Currently, there are no donations. ")
    else:
        for donations in donations:
            print(donations)
