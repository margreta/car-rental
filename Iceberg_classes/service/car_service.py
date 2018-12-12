from repository.car_repo import Car_Repo

class Car_Service:

    def __init__(self):
        self.__car_repos = Car_Repo()

    def add_cars(self, cars):
        if self.is_valid_car(cars):
            self.__car_repos.add_cars(cars)
    
    def is_valid_car(self, cars):
        return True

    # def get_cars(self):
    #     return self.__car_repos.get_cars()
    
    #cb = create booking.
    def cb_show_available_cars(self, inp_car_type):
        return self.__car_repos.cb_show_available_cars(inp_car_type)