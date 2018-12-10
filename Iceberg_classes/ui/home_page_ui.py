from getpass import getpass


from service.home_service import Home_service

class Home_page:

    def __init__(self):
        self.home_service = Home_service()

    def home(self):
        """prints the homepage and prompts for user to choose an operator"""
        
        #Header:
        print("HOME")
        print("-" * 20)

        #Define the user:
        print("Who are you?")
        print("1. Admin\n2. Dealer\n")
        user = input("Please press 1, 2 or 3 to make your pick: ")
        return user
    
    def log_in(self,user):
        """prints the log-in site and prompts for username and password"""
    
        #Header:
        print("LOG IN")
        print("-" * 20)

        username = " "
        while username != "dealer" and username != "admin":
            try: 
                username = input("Username: ")
                password = getpass("Password: ")
                print("")
                self.home_service.log_in(user,username)
            except:
                print("Invalid log in, please try again!")
                username = " "
        
        return username





        
            