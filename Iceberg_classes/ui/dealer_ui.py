
from service.dealer_service import Dealer_service

class Dealer_Ui:
    def __init__(self):
        self.dealer_service = Dealer_service()
    
    def home_page(self):
        #Header:
        print("DEALER")
        print("-" *20)
        
        choice = 7
        while choice not in range(1,6):
            try: 
                print("Please choose an action: ")
                choice = int(input("1. Create booking\n2. Change booking\n3. Return rental\n4. Overview\n5. Go back\n"))
                print("")
                self.dealer_service.home_check(choice)
            except: 
                print("Not a valid option, please select number from 1 to 5")
                print("")
        return choice

    def create_booking_1_of_5(self):
        """creates both the customer and his booking, this is the first page of five in this process"""

        #Header:
        print("DEALER/ Create booking")
        print("-" * 20)
        print("(1 of 5)")


        name_alpha = False
        while name_alpha == False:
            try: 
                name = input("Enter name of customer: ")
                name_alpha = name.isalpha()
                self.dealer_service.cb_check_name(name_alpha)
            except: 
                print("Name cannot include numbers, please try again!")
                print("")

        driver = False
        while driver == False:
            try: 
                driver_license = input("Enter a driver's license number: ")
                driver = driver_license.isnumeric()
                self.dealer_service.cb_check_driver_license(driver)
            except:  
                print("Driver license needs to be all digits and 9 characters, please try again!")
                print("")
            
        email = False
        while email == False:
            try: 
                email = input("Enter the clients email: ")
                self.dealer_service.cb_check_email(email)
            except: 
                print("Email needs to include '@', please try again!")
                print("")
                email = False

        phone_num = False
        while phone_num == False:
            try: 
                phone_num = input("Enter the customers phone number: ")
                phone_num = phone_num.isnumeric()
                self.dealer_service.cb_check_phone(phone_num)
            except:
                print("Phone number needs to be all numbers, please try again!")
        return name,driver_license,email,phone_num

    def confirm_customer(self, name):
        confirm = input("Confirm customer information? (y/n) ".lower())
        print("")
        if confirm == "y":
            print("{} has been added to system".format(name.capitalize()))
        elif confirm == "n":
            print("Please choose action from the options list.")
            print("")
        return confirm
    
    def options(self):
        print("Options: ")
        contin = input("1. Continue\n2. Go back\n3. Go to homepage")
        return contin
    
    def create_booking_2_of_5(self):
        #Header:
        print("DEALER/ Create booking")
        print("-" * 20)
        print("(2 of 5)")
        print("The insurance of the rent")
        print("")

#Needs to validate these information
        card_num = input("Enter the card number: ")
        valid = input("Enter the validation time (MM/YY): ")
        cvc = input("Enter CVC: ")

        print("Card information has been saved for {}".format(name.capitalize()))

        return card_num, valid, cvc



