import csv
from models.car import Car
from models.booking import Booking

class Booking_Repo: 
    # def __init__(self):
    #     self.car = []
    #     self.booking = []
        

    #Overview action.
    def look_up_customer(self, custom_email):
        with open("./data/booking.csv") as booking_file:
            for line in booking_file:
                name,drivers_license,email,phone_number,credit_card_insurance,start_date, end_date,license_plate,types,price,extras,payment_type,booking_status = line.strip().split(",")
                if email == custom_email:
                    print(line)

    
