import csv
from models.car import Car 


class Look_in_data:
    
    def show_available_cars(self, car_choice):
        with open("./data/car.csv", "r") as cars_file:
            for line in cars_file.readlines():
                license_num, car_type, price, status = line.strip().split(",")
                if car_choice == 1:
                    if status == "Available":
                        print("{:<13}{:<6}{:<7}{:<10}".format(license_num, car_type, price, status))
                elif car_choice == 2:
                    if status == "Rented":
                        print("{:<13}{:<6}{:<7}{:<10}".format(license_num, car_type, price, status))

    def look_up_car(self, car_choice, license_number):
        with open("./data/car.csv", "r") as cars_file:
            for line in cars_file.readlines():
                license_num, car_type, price, status = line.strip().split(",")
                if car_choice == 3:
                    if license_num == license_number:
                        return print("{:<13}{:<6}{:<7}{:<10}".format(license_num, car_type, price, status))
                    elif license_num != license_number:
                        pass
                        

    def look_up_customer(self, custom_email):
        with open("./data/booking.csv", "r") as client_file:
            for line in client_file.readlines():
                name,drivers_license,email,phone_number,credit_card_insurance,start_date, end_date,license_plate,types,price,extras,payment_type = line.strip().split(",")
                if email == custom_email:
                    print(line)
                    
        



                    
        
