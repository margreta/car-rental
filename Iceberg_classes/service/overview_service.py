import csv
from repository.car_repo import Car_Repo
from repository.booking_repo import Booking_Repo

#c = car/customer:
class Look_up_c:
    def __init__(self):
        self.__cars_repo = Car_Repo()
        self.__booking_repo = Booking_Repo()
    
    def overview_check(self, choice):
        if choice not in range(1,4):
            raise Exception

    def get_customer(self,custom_email):
        valid_email = self.__booking_repo.look_up_customer(custom_email)
        # raise Exception

    def car_menu_check(self, choice):
        if choice not in range (1,6):
            raise Exception

    def get_cars(self, car_choice):
        return self.__cars_repo.show_available_cars(car_choice)
    
    def valid_license_plate(self, car_choice, license_number):
        self.__cars_repo.look_up_car(car_choice, license_number)
        if license_number == False:
            raise Exception
        