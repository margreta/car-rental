
from models.car import Car

class Data_Access: 
    def __init__(self):
        self.car = []
        self.booking = []
        


    def show_available_cars(self):
        
        with open("car.csv", "r") as cars_file:
            for line in cars_file.readlines():
                license_num, car_type, price, status = line.strip().split(",")
            
                if status == "Available":
                    print(line)   
    
