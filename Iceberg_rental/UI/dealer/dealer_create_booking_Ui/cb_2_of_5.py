from getpass import getpass

from Ui.dealer.dealer_create_booking_Ui.create_booking_1_of_5 import create_booking_1_of_5

def create_booking_2_of_5():
    #Header:
    print("DEALER/ Create booking")
    print("-" * 20)
    print("(2 of 5)")
    print("The insurance of the rent")

    card_num = input("Enter the card number: ")
    valid = input("Enter the validation time (MM/YY): ")
    cvc = input("Enter CVC: ")

    print("Card information has been saved for {}".format(name.capitalize()))

    #options for next action:
    print("Options: ")
    choice = getpass("1. Continue\n2. Go back\n3. Go to homepage")

