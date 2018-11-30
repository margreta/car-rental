from getpass import getpass

def homepage():
    print("HOME")
    print("-" *20)
    print("Who are you?")
    print("1. Admin\n2. Dealer\n3. Customer")
    user = input("Please press 1, 2 or 3 to make your pick: ")
    return user

def login():
    print("LOG IN")
    print("-" *20)
    username = input("Username: ")
    password = getpass("Password: ")
    return username, password

def welcome(username, password):
    if username == "admin":
        printline = "Admin"
    elif username == "dealer":
        printline = "Dealer"
    print("Welcome {}!".format(printline))

def admin():
    print("ADMIN/Create new car")
    print("-" *20)
    print("Choose action: ")
    choice = getpass("1. Create new car\n2. Remove car\n3. Mark car for repair\n4. Go back\n ")
    print("")
    if choice == "1":
        again = create_car()
    elif choice == "2":
        remove_car()
    elif choice == "3":
        mark_repair
    elif choice == "4":
        pass

def remove_car():
    print("ADMIN/Remove car")
    print("-" *20)
    license_num = input("Please enter license plate number of car to remove from system: ")
    confirm = input("Are you sure you want to remove {} from system?".format(license_num))
    print("{} has been removed from system".format(license_num))
    print("")
    again = input("Do you want to remove another car? (y/n)")
    
def mark_repair():
    pass

def create_car(): 
    print("ADMIN/Remove car")
    print("-" *20)
    car_type = input("Please enter car type (Type A, Type B, Type C) :")
    license_num = input("Please enter license plate number: ")
    print("")
    confirm = input("Confirm this car registration? (y/n) ")
    print("")
    print("The car {} has been added to system.".format(license_num))
    print("")
    again = input("Would you like to add another car? (y/n)")
    return again

def dealer():
    print("DEALER")
    print("-" *20)
    choice = input("1. Create booking\n2. Change booking\n3. Return rental\n4. Overview\n5. Go back")

    


user = homepage()
print("")
username, password = login()
welcome(username, password)
print("")
if user == "1": 
    admin()
elif user == "2": 
    dealer()

