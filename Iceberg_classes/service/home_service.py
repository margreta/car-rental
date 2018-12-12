from repository.car_repo import Car_Repo

class Home_service:
    def __init__(self):
        self.car_repo = Car_Repo
    
    def log_in(self,user,username):
        if user == "1":
            if username != "admin":
                raise Exception
        elif user == "2":
            if username != "dealer":
                raise Exception

    
        
    

        
        

            
