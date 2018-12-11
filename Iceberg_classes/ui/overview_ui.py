from service.overview_service import Look_up_c
from models.booking import Booking


class Overview_Ui:
    def __init__(self):
        self.__look_up_customer = Look_up_c()
        self.__model_booking = Booking

    def overview_menu(self): 
        """the overview menu where the dealer can choose what he wants to review and see"""
        print("Dealer / Overview")
        print("-" * 20)
        choice = 7
        while choice not in range(1,4):
            try:
                print("Please choose 1, 2 or 3.")
                choice = int(input("1. Look up customer\n2. Car information\n3. Go back\n"))
                self.__look_up_customer.overview_check(choice) #hér þarf að runna í service fallinu.
            except:                
                print("Not a valid option, please select number from 1 to 3")
                print("")
        return choice
    
    def look_up_customer(self):
        email = False
        while email == False:
            try:
                custom_email = input("Please enter email of customer to find in system: ")
                self.__look_up_customer.get_customer(custom_email)
                break
            except:
                print("Not a valid email, please enter a valid email.")
                print("")
        
    def car_overview(self):
            # elif choice == "2":
        car_choice = 7
        while car_choice not in range (1,6):
            try:
                print("Choose action:")
                print("")
                car_choice = int(input("1. Show all available cars\n2. Show rented cars\n3. Look up a specific car\n4. Show price list\n5. Go back\n"))
                self.__look_up_customer.car_menu_check(car_choice) #hér þarf að kalla í eitthvað í service fallinu
            except:
                print("Not a valid option, please select number from 1 to 5")
                print("")
        return car_choice

    def specific_car_input(self, car_choice):
        license_num = False
        while license_num == False:
            try:
                license_number = input("Insert license plate: ")
                self.__look_up_customer.valid_license_plate(car_choice,license_number)
                license_num = True
            except:
                print("License plate number does not exist in the system, please enter a valid number.")
                print("")
        return license_number

    def show_price_list(self):
        print("Prices are per day.")
        print(" "*2,"Type A"," "*8,"Type B"," "*8, "Type C"," "*2)
        print("-"*44)
        print(" "*2,"$4000"," "*9,"$3000"," "*9, "$2000"," "*2)
        print("")
        print("Extras:")
        print("")
        print("Kasko insurance ($50)\nChild seat ($1)")
        print("")        



    def go_back(self):
        print("Options:\n1. Go to Dealer home page.")
        choice_back = input()

