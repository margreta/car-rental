import csv
from models.car import Car
from models.booking import Booking

class Booking_Repo: 
      
    #Overview action.
    def look_up_customer(self, custom_email):
        with open("./data/booking.csv", encoding="utf-8") as booking_file:
            header = []
            for line in booking_file:
                list_line = line.strip().split(",")
                file_email = list_line[2]
                if file_email == "Email":
                    header.extend(list_line)
                if file_email == custom_email:
                    for x in range(13): 
                        print("{:>21}  {:<25}".format(header[x],list_line[x]))
    
