
from repository.car_repo import Car_Repo

class Dealer_service:
    def __init__(self):
        self.car_repo = Car_Repo()

    def home_check(self, choice):
        if choice not in range(1,6):
            raise Exception
    
    def cb_check_name(self,name_alpha):
        if name_alpha is False: 
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


    # def extras(self):

    

    # def show_available_cars(self, inp_car_type):
    #     self.car_repo.show_available_cars(inp_car_type)



        


