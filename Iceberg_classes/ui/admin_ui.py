from service.admin_service import Admin_service
from service.car_service import Car_Service
from repository.car_repo import Car_Repo
from models.car import Car

class Admin_Ui:
    def __init__(self):
        self.admin_service = Admin_service()
        self.__car_service = Car_Service()

    def admin_home_page(self):
        """interface that admin can access"""
        #Header
        print("ADMIN")
        print("-" *20)

        print("Choose action: ")
        
        choice = 7
        while choice not in range(1,5):
            try: 
                choice = int(input("1. Create new car\n2. Remove car\n3. Mark car for repair\n4. Go back\n "))
                print("")
                self.admin_service.home_check(choice)
            except:
                print("Invalid action, please select number from 1 to 4")
                print("")
        return choice
    
    def remove_car(self):
        #Header
        print("ADMIN/Remove car")
        print("-" *20)
# Validation tests need to be added in admin_service
        license_num = input("Please enter license plate number of car to remove from system: ").upper()
        confirm = input("Are you sure you want to remove {} from system? (y/n) ".format(license_num)).lower()

        print("{} has been removed from system".format(license_num.upper()))
        print("")

        again = input("Do you want to remove another car? (y/n)")
        getting = Car_Repo()
        getting.remove_car(license_num)    

    def mark_repair(self):
        print("Choose action: ")
        repair_choice = input("1. Mark in repair\n2. Mark out of repair\n ")
        repeat = "y"
        sure = "n"
        while repeat == "y":
            while sure == "n":
                license_num = input("Pleace enter the License plate number of car to mark for repair: ").upper()
                sure = input ("Are you sure you want to mark {0} unavalible due to repair? (y/n) ".format(license_num)).lower()
                repeat = input("Would you like to mark anathor car for repair? (y/n) ").lower()
        getting = Car_Repo()
        getting.mark_repair(repair_choice,license_num)    
        
        

    def create_car_page(self): 
        print("ADMIN/Create new car")
        print("-" *20)

        license_num = input("Please enter license plate number: ")
        #needs to add price depending on car type (if, else)
        car_type = input("Please enter car type (A, B, C) :")
        print("")

        confirm = input("Confirm this car registration? (y/n) ")
        print("")
        print("The car {} has been added to system.".format(license_num.upper()))
        print("")

        again = input("Would you like to add another car? (y/n)")
        return license_num, car_type, confirm, again

    def create_the_car(self, license_num, car_type, price, status = "Available"):
        new_car = Car(license_num, car_type, price, status)
        self.__car_service.add_cars(new_car)
        