
import datetime
from service.dealer_service import Dealer_service
from service.car_service import Car_Service
from service.admin_service import Admin_service
from models.car import Car

class Dealer_Ui:
    def __init__(self):
        self.dealer_service = Dealer_service()
        self.__car_service = Car_Service()
        self.admin_service = Admin_service()
    
    def home_page(self):
        #Header:
        print("DEALER")
        print("-" *20)
        
        choice = 7
        while choice not in range(1,6):
            try: 
                print("Please choose an action: ")
                choice = int(input("1. Create booking\n2. Change booking\n3. Return rental\n4. Overview\n5. Log out\n"))
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

        last_name_alpha = False
        first_name_alpha = False
        while first_name_alpha == False or last_name_alpha == False: 
            try: 
                first_name= input("Enter first name: ").capitalize()
                last_name = input("Enter last name: ").capitalize()
                first_name_alpha = first_name.isalpha()
                last_name_alpha = last_name.isalpha()
                self.dealer_service.cb_check_name(first_name_alpha, last_name_alpha)
            except: 
                print("Name cannot include numbers or spaces, please enter first name and last name seperately!")
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
                print("Phone number needs to be all numbers, please try again!\n")
        print("")
        return first_name, last_name, driver_license, email, phone_num

    def confirm_customer(self, first_name, last_name):
        confirm = input("Confirm customer information? (y/n)".lower())
        if confirm == "y":
            print("{} {} has been added to system\n".format(first_name.capitalize(), last_name.capitalize()))
        elif confirm == "n":
            print("Please choose action from the options list\n.")
        return confirm
    
    def options(self):
        print("Options: ")
        contin = input("1. Continue\n2. Go back\n3. Go to homepage\n")
        print("")
        return contin
        
    def create_booking_2_of_5(self,name):
        #Header:
        print("DEALER/ Create booking")
        print("-" * 20)
        print("(2 of 5)")
        print("The insurance of the rent\n")
        
        card = False
        while card == False:
            try: 
                card_num = input("Enter the card number : ")
                self.dealer_service.cb_check_card_num(card_num)
                card = True
            except:
                print("Card number has 16 numbers, please do not use space or '-' between numbers.")
        is_valid = False
        while is_valid == False:
            try: 
                validation_date= input("Enter the validation time (M/YY): ")
                self.dealer_service.check_if_card_is_valid(validation_date)
                is_valid = True
            except:
                print("Card is outdated, please use card with valid validation time.")
        cvc = False
        while cvc == False:
            try: 
                cvc_num = input("Enter CVC: \nThree numbers positioned on the back of the card.")
                self.dealer_service.cb_check_cvc(cvc_num)
                cvc = True
            except: 
                print("The cvc is three digits, all numbers, please try again!\n")

        print("Card information has been saved for {}\n".format(name))
        return card_num, validation_date, cvc


    def create_booking_3_of_5(self):
        #Header:
        print("DEALER/ Create booking")
        print("-" * 20)
        print("(3 of 5)")

        print("Please select date")
        print("")

        start_date = input("Enter start date (D/M/YYYY): ")
        amount_of_days = int(input("Amount of days: "))
        print("")
       
        inp_car_type = " "
        while inp_car_type not in "ABC":
            try:
                inp_car_type = input("Car type A = $4000 \nCar type B = $3000 \nCar type C = $2000\nSelect a car type (A, B, C): ").upper()
                print("")
                self.admin_service.car_type_check(inp_car_type)
            except: 
                print("Available types are A, B or C. Please choose one of those types!\n")
        return start_date, amount_of_days, inp_car_type 

    def print_end_date(self,end_date):
        print("End date of the rent: ", end_date)
        
       

    def create_booking_4_of_5(self,inp_car_type):
        #Header:
        print("DEALER/ Create booking/ Show all available cars")
        print("-" * 20)
        print("(4 of 5)\n")
        print("Print available cars\n")

        print("{:<13}{:<6}{:<7}{:<10}".format("Car lic.", "Type", "Price", "Car status"))
        print("-" * 36)
        self.__car_service.show_available_cars(inp_car_type)
        print("")

        print("Extras: ")

    def extras(self):
        kasko_or_child_seat = input("1. Kasko insurance\n2. Child seat\n")
        more_extras = input("More extras? (y/n)")
        print("")
        return kasko_or_child_seat, more_extras

        
    def create_booking_5_of_5(self):
        #Header:
        print("DEALER/ Create booking/ Billing type")
        print("-" * 20)
        print("(5 of 5)\n")
        
        print("Please choose billing type\n")
        billing_type = input("1. Credit or debit card\n2. Billing to\n3. Cash\n4. Go back\n5. Go to home page\n")
        return billing_type

    def credit_debit_card(self):
        card_name = input("Enter name of carholder: ")
        card_number = input("Enter card number: ")
        validation_time = input("Enter validation time (MM/YY)")
            # Setja hér tékk hvort validation_time sé "stærri" tala en dagurinn í dag 
            # ef svo er þá kemur villa að kortið sé útrunnið
        return card_name, card_number, validation_time

    def confirm_billing(self):
        confirm = input("Confirm payment? (y/n)")
        if confirm == "y":
            print("Your payment has been made.")
        elif confirm == "n":
            print("You didn't confirm the payment, you'll be transported back to choose a billing type.\n") 
        return confirm 
        
    def billing_to(self):
        comp_name = input("Enter name of company: ")
        amount = input("Enter amount to charge: ") 
        due_date = input("Enter due date (D/M/YYYY): ")
        return comp_name, amount, due_date

    def cash(self, total_amount):
        print("Amount due: {}\n".format(total_amount))
        paid_amount = input("Enter amount paid: ")
        return paid_amount

    def print_change(self, change):
        print("Change: {}".format(change))












        
##################################################################################################################

 



