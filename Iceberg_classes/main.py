from ui.home_page_ui import Home_page
from ui.dealer_ui import Dealer_Ui
from ui.admin_ui import Admin_Ui
from models.car import Car


def main():
    ui = Home_page()
    user = ui.home()
    username = ui.log_in(user)

    dealer_ui = Dealer_Ui()
    admin_ui = Admin_Ui()

    if username == "dealer":
        choice = dealer_ui.home_page()
        if choice == 1: 
            confirm = "n"
            while confirm == "n":
                name, driver_license, email, phone_num = dealer_ui.create_booking_1_of_5()
                confirm = dealer_ui.confirm_customer(name)
                contin = dealer_ui.options()
                if contin == "1":
                    card_num, valid, cvc = dealer_ui.create_booking_2_of_5()
                elif contin == "2":
                    continue
                elif contin == "3":
                    dealer_ui.home_page()


        # if choice == 2:
            

    
    elif username == "admin":
        choice = admin_ui.admin_home_page()
        if choice == 1:
            admin_ui.create_car()
        elif choice == 2:
            admin_ui.remove_car()
        elif choice == 3:
            admin_ui.mark_repair()
        elif choice == 4:
            Home_page.home
        







    



    


main()