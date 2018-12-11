from ui.home_page_ui import Home_page
from ui.dealer_ui import Dealer_Ui
from ui.admin_ui import Admin_Ui
from models.car import Car

def car_type_price(inp_car_type):
    if inp_car_type == "A":
        price = 4000
    elif inp_car_type == "B":
        price = 3000
    elif inp_car_type == "C":
        price = 2000 
    return price 


def main():
    ui = Home_page()
    user = ui.home()
    username = ui.log_in(user)

    dealer_ui = Dealer_Ui()
    admin_ui = Admin_Ui()

    go_to_homepage = "y"
    while go_to_homepage == "y":
        if username == "dealer":
            choice = dealer_ui.home_page()
            if choice == 1: 
                #initializing variables: 
                repeat = "y"
                confirm = "n"
                skip_option = "n"

                while repeat == "y":
                    while confirm == "n":
                        name, driver_license, email, phone_num = dealer_ui.create_booking_1_of_5()
                        confirm = dealer_ui.confirm_customer(name)
                        current_page = 1
                    
                    if skip_option == "n":
                        contin = dealer_ui.options()
                
                    if contin == "1":
                        if current_page == 1:
                            card_num, valid, cvc = dealer_ui.create_booking_2_of_5(name)
                            current_page += 1

                        elif current_page == 2:
                            start_date, amount_of_days, inp_car_type = dealer_ui.create_booking_3_of_5()
                            price = car_type_price(inp_car_type)
                            current_page += 1

                        elif current_page == 3: 
                            #initiate the price counter: 
                            total_price = 0 
                            skip_option = "n"

                            dealer_ui.create_booking_4_of_5(inp_car_type)
                            more_extras = "y"
                            while more_extras == "y":
                                kasko_or_child_seat, more_extras = dealer_ui.extras()
                                if kasko_or_child_seat == "1": 
                                    total_price += 1
                                elif kasko_or_child_seat == "2":
                                    total_price += 50
                            current_page += 1

                        elif current_page == 4:
                            #Get total amount to charge:
                            total_amount = price + total_price
                            #How is customer paying:
                            billing_type = dealer_ui.create_booking_5_of_5()
                            
                            if billing_type == "1":
                                card_name, card_number, validation_time = dealer_ui.credit_debit_card()
                            elif billing_type == "2":
                                comp_name, amount, due_date = dealer_ui.billing_to()
                            elif billing_type == "3":
                                paid_amount = int(dealer_ui.cash(total_amount))
                                change = total_amount - paid_amount
                                dealer_ui.print_change(change)
                            elif billing_type == "4":
                                current_page -= 1
                                skip_option = "y"
                            elif billing_type == "5":
                                confirm = "n"
                                continue
                            if billing_type in "1,2,3":
                                again = dealer_ui.confirm_billing()
                                if again == "n":
                                    #Start over:
                                    skip_option = "y"
                                    continue
                        
                    elif contin == "2":
                        if current_page == 1: 
                            go_to_homepage = "y"
                            break
                        elif current_page == 2: 
                            confirm = "n"
                            skip_option = "n"
                            continue
                        elif current_page == 3: 
                            current_page -= 1
                            confirm = "y"
                            skip_option = "y"
                            continue
                        elif current_page == 4: 
                            current_page -=1
                            continue
                        # confirm = "n"
                        # continue
                    elif contin == "3":
                        go_to_homepage = "y"
                        continue

        # if choice == 2:
            #Næsta aðgerð fyrir dealer (change booking) 

        
        elif username == "admin":
            choice = admin_ui.admin_home_page()
            if choice == 1:
                admin_ui.create_car()
            elif choice == 2:
                admin_ui.remove_car()
            elif choice == 3:
                admin_ui.mark_repair()
main()        