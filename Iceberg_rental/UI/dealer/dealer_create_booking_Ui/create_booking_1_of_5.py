from getpass import getpass

from Ui.dealer.dealer_create_booking_Ui.cb_2_of_5 import 

def create_booking_1_of_5():
    """creates both the customer and his booking in 5 "pages" in the system"""

    #Header:
    print("DEALER/ Create booking")
    print("-" * 20)
    print("(1 of 5)")

    #Get information about customer (1 of 5)
    name = input("Enter name of customer: ")
    driverlicense = input("Enter a driver's license number: ")
    email _ input("Enter the clients email: ")
    phone_num = input("Enter the customers phone number: ")
    print("")

    confirm = input("Confirm customer information? (y/n) ")

    print("{} has been added to system".format(name.capitalize()))
    print("")

    #options for next action:
    print("Options: ")
    choice = getpass("1. Continue\n2. Go back\n3. Go to homepage")

    if choice  == "1":
        
