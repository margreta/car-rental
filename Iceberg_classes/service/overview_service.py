import csv
from repository.look_up_data import Look_in_data

#c = car/customer:
class Look_up_c:
    def __init__(self):
        self.__cars_repo = Look_in_data()
    
    def overview_check(self, choice):
        if choice not in range(1,4):
            raise Exception

    def get_customer(self,custom_email):
        self.__cars_repo.look_up_customer(custom_email)
        if custom_email in self.__cars_repo.look_up_customer(custom_email):
            for letter in custom_email:
                if letter == "@":
                    email = True
                    break
                else:
                    email = False
            if custom_email == "@":
                email = False        
        
        elif custom_email not in self.__cars_repo.look_up_customer(custom_email):
            raise Exception

    def car_menu_check(self, choice):
        if choice not in range (1,6):
            raise Exception

    def get_cars(self, car_choice):
        return self.__cars_repo.show_available_cars(car_choice)
    
    def valid_license_plate(self, car_choice, license_number):
        self.__cars_repo.look_up_car(car_choice, license_number)
        if license_number == False:
            raise Exception
        