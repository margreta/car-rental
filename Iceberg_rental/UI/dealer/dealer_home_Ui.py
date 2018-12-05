from getpass import getpass

from Ui.dealer.dealer_create_booking_Ui.cb_2_of_5 import create_booking_2_of_5

def dealer():
    #Header:
    print("DEALER")
    print("-" *20)

    #prompt for action from user:
    choice = getpass("1. Create booking\n2. Change booking\n3. Return rental\n4. Overview\n5. Go back")

    if choice == "1":
        create_booking_2_of_5()
    # elif choice == "2":
    #     change_booking()

