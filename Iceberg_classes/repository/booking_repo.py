import csv
import os

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
    
    def cancel_booking(self,name):
        with open("./data/booking.csv", "r+",encoding = "utf-8") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            with open("./data/new_booking.csv", "a+") as new_file:
                fieldnames = ["Name", "Drivers_license", "Email","Phone_number","Credit_card_insurance","Start_date","End_date","License_plate","Types","Price","Extras","Payment_type","Booking_status"]
                csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames)
                csv_writer.writeheader()

                for line in csv_reader:
                    if name in line.values():
                        line["Booking_status"] = "Cancelled"
                        csv_writer.writerow(line)
                    else:
                        csv_writer.writerow(line)

            os.remove("./data/booking.csv")
            os.rename("./data/new_booking.csv","./data/booking.csv")