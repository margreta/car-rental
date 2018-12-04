class Car: 
    def __init__(self, car_type, license_num, status):
        self.car_type = car_type
        self.license_num = license_num
        self.status = status

    def get_car_type(self):
        self.car_type = car_type

    def get_status(self):
        self.status = status

    def get_license_num(self):
        self.license_num = license_num

    def __str__(self):
        return "{}, {}, {}".format(self.car_type, self.license_num, self.status)


