from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register
database = {"admin": "123"}
donations = []
authorized_user = str()

if authorized_user == str():
    print("You must be logged in to donate.")
else:
    print("Logged in as: ", authorized_user)

while True:
    show_homepage()
    option = input("Chose an option: ")

    if option == "1":
        username = input("\nEnter your username: ")
        password = input("\nEnter your password: ")
        authorized_user = login(database, username, password)

    elif option == "2":
        username = input("\nEnter your username: ")
        password = input("\nEnter your password: ")
        authorized_user = register(database, username)
        if authorized_user != str():
            database[username] = password
        continue

    elif option == "3":
        if authorized_user == str():
            print("\nYou are not logged in")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
        continue

    elif option == "4":
        show_donations(donations)

    elif option == "5":
        print("\n\n\nLeaving DonateMe...")
        break
