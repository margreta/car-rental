class Car: 
    def __init__(self, car_class, license_num, status):
        self.car_class = car_class
        self.license_num = license_num
        self.status = status

    def get_status(self):
        self.status = status
    def get_license_num(self):
        self.license_num = license_num

    def mark_in_repair(self, license_num):
        self.license_num = 10

    def remove(self,license_num):
        self.license_num = 0  