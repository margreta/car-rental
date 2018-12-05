from getpass import getpass

def login(user):
    """prints the log-in site and prompts for username and password"""
    #Header:
    print("LOG IN")
    print("-" * 20)

    while True:
        username = input("Username: ")
        password = getpass("Password: ")
        if user == "1":
            if username != "admin":
                error = True
                print("")
            elif username == "admin":
                print("")
                error = False
        elif user == "2":
            if username != "dealer":
                error = True
                print("")
            elif username == "dealer":
                print("")
                error = False

        if error:
            print("Wrong username or password, please try again!")
        elif error == False: 
            print("Welcome {}!".format(username.capitalize()))
            break
    return username, password



