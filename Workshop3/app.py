from donations_pkg.homepage import show_homepage
from donations_pkg.user import login
database = {"admin": "password123"}
donations = []
authorized_user = str()


while True:

    show_homepage()

    if authorized_user is str():
        print("You must be logged in to donate.")
    if authorized_user is not str():
        print("Logged in as: ", authorized_user)

    option = input("Chose an option: ")

    if option == "1":
        username = input("\nEnter your username: ")
        password = input("\nEnter your password: ")
        authorized_user = login(username, password, database)

    elif option == "2":
        print("TODO: Write Register Functionality\n")
        continue

    elif option == "3":
        print("TODO: Write Donate Functionality\n")
        continue

    elif option == "4":
        print("TODO: Write Show Donations Functionality\n")
        continue

    elif option == "5":
        print("\n\n\nLeaving DonateMe...")
        break
