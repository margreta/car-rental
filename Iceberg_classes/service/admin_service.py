from repository.car_repo import Car_Repo


class Admin_service:
    def __init__(self):
        self.car_repo = Car_Repo

    def home_check(self, choice):
        if choice not in range(1,6):
            raise Exception
