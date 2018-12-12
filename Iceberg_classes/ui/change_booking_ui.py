from service.dealer_service import Dealer_service

class Change_Booking_Ui:

    def __init__(self):
        self.__dealer_service = Dealer_service()
    
    def change_booking_menu(self):
        change_choice = 7
        while change_choice not in range (1,4):
            try:
                print("Choose action:")
                print("")
                change_choice = int(input("1. Edit booking\n2. Cancel booking\n3. Go back\n"))
                self.__dealer_service.change_check(change_choice)#hér þarf að kalla í eitthvað í service fallinu
            except:
                print("Not a valid option, please select number from 1 to 3")
                print("")
        return change_choice
    
    def edit_booking(self):
        pass

    def cancel_booking(self):
        name = False
        while name == False:
            try:
                print("Enter name of cancelling customer: ")
                first_name = input("First name: ")
                last_name = input("Last name: ")
                name = first_name.capitalize() + " " + last_name.capitalize()
                self.__dealer_service.cancel_check(name)# kalla í service fall
                print("{} booking has been cancelled".format(name))
                print("")
                name = True
            except:
                print("This name does not exist in the system, please try again.")
                print("")
        return name