from repository.data_access import Data_Access

class Home_service:
    def __init__(self):
        self.data_access = Data_Access()
    
    def log_in(self,user,username):
        if user == "1":
            if username != "admin":
                raise Exception
        elif user == "2":
            if username != "dealer":
                raise Exception

    
        
    

        
        

            
