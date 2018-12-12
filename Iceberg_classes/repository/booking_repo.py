
from models.car import Car

class Booking_Repo: 
    def __init__(self):
        self.car = []
        self.booking = []
        

    #Overview action.
    def look_up_customer(self, custom_email):
        with open("./data/booking.csv", "r") as client_file:
            for line in client_file.readlines():
                name,drivers_license,email,phone_number,credit_card_insurance,start_date, end_date,license_plate,types,price,status,extras,payment_type = line.strip().split(",")
                if email == custom_email:
                    print(line)

    
