def login(database, username, password):

    for key, value in database:
        if key == username and value == password:
            print("\nWelcome ", username)
            return username

        elif key != username and value == password:
            print("\nIncorrect password for ", username)
            return str()
        else:
            key != username and value != password
            print("\nUser not found. Please register")
            return str()
