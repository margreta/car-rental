import csv
from models.car import Car

class Car_Repo:

    def __init__(self):
        self.__cars = []

    def add_cars(self, car):
        with open("./data/car.csv", "a+") as cars_file:
            license_num = car.get_license_num()
            car_type = car.get_car_type()
            price = car.get_price()
            status = car.get_status()
            cars_file.write("\n{},{},{},{}".format(license_num.upper(), car_type.upper(),price, status))

    def mark_repair(self, repair_choice, license_num):
        with open("./data/car.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            with open("./data/new_cars.csv", "w") as new_file:
                fieldnames = ["License_plate", "Type", "Price","Status"]

                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

                csv_writer.writeheader()

                for line in csv_reader:
                    if repair_choice == "1":
                        if license_num in line.values():
                            line["Status"] = "Unavailable"
                            csv_writer.writerow(line)
                            csv_writer.writerow(line)
                    elif repair_choice == "2":
                        if license_num in line.values():
                            line["Status"] = "Available"
                            csv_writer.writerow(line)
                        else:
                            csv_writer.writerow(line)

    def remove_car(self, license_num):

        with open("./data/car.csv", "rw") as csv_file:
            csv_reader = csv.DictReader(csv_file)

            with open("./data/car.csv", "w") as new_file:
                fieldnames = ["License_plate", "Type", "Price","Status"]

                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

                csv_writer.writeheader()

                for line in csv_reader:
                    if license_num in line.values():
                        del line
                    else:
                        csv_writer.writerow(line)

    def show_available_cars(self, inp_car_type):
        
        with open("./data/car.csv", "r") as cars_file:
            for line in cars_file.readlines():
                license_num, car_type, price, status = line.strip().split(",")
            
                if status == "Available" and car_type == inp_car_type:
                    print("{:<13}{:<6}{:<7}{:<10}".format(license_num, car_type, price, status))
    
    