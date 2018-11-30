# from admin import Admin
# from car import Car
# from dealer import Dealer
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
    print("Choose action: ")
    choice = input("1. Create new car\n2. Remove car\n3. Mark car for repair\n4. Go back\n")
    return choice



def dealer():
    print("DEALER")
    print("-" *20)
    choice = input("1.")
    


user = homepage()
print("")
username, password = login()
welcome(username, password)
print("")
if user == "1": 
    admin()
elif user == "2": 
    dealer()

