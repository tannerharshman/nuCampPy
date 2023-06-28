def login(database, username, password):

    if username in database:
        if database[username] == password:
            print(f"\nWelcome, {username}!\n")
            return username

        else:
            print("\nIncorrect password.\n")
            return str()
    else:
        print("\nUsername not found. Please register\n")
        return str()


def register(database, username):
    if username in database:
        print(f"\nUsername {username} already registered.")
    else:
        print(f"\nUsername {username} has been registered.")
        return username
