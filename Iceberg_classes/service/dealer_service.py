import datetime
from repository.car_repo import Car_Repo
from repository.booking_repo import Booking_Repo

class Dealer_service:
    def __init__(self):
        self.car_repo = Car_Repo()
        self.booking_repo = Booking_Repo()

    def home_check(self, choice):
        if choice not in range(1,6):
            raise Exception

    #cb = Create booking. 
    def cb_check_name(self,first_name_alpha, last_name_alpha):       
        if first_name_alpha == False or last_name_alpha == False: 
            raise Exception

    def cb_check_driver_license(self, driver):
        if driver == False:
            raise Exception
        
    def cb_check_email(self,email):
        for letter in email: 
            if letter == "@": 
                email = True
                break
            else:
                email = False
        
        if email == False:
            raise Exception
    
    def cb_check_phone(self, phone_num):
        if phone_num == False:
            raise Exception

    def cb_check_card_num(self, card_num):
        len_card_num = len(card_num)
        card_num_numeric = card_num.isnumeric()
        if len_card_num < 16 or len_card_num > 16:
            raise Exception
        if card_num_numeric == False:
            raise Exception


    def check_if_card_is_valid(self, validation_date): 
        tday = datetime.datetime.today()
        dt = datetime.datetime.strptime(validation_date, "%m/%y")
        end_date = dt - tday
        difference = end_date.days
        if difference < 0:
            raise Exception

    def cb_check_cvc(self,cvc):
        len_cvc = len(cvc)
        cvc_numeric = cvc.isnumeric()
        if len_cvc < 3 or len_cvc > 3: 
            raise Exception
        if cvc_numeric == False:
            raise Exception

    def valid_return(self, license_num):
        if license_num == False:
            raise Exception
        self.car_repo.return_rental(license_num)

    #Change booking.
    def change_check(self, change_choice):
        if change_choice not in range (1,4):
            raise Exception

    def edit_check(self):
        pass

    def cancel_check(self, name):
        if name == False:
            raise Exception
        self.booking_repo.cancel_booking(name)

        


