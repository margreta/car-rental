from getpass import getpass

from Ui.home_page_Ui import home_page
from Ui.log_in_Ui import login

from Ui.dealer.dealer_create_booking_Ui.create_booking_1_of_5 import create_booking_1_of_5



user = home_page()
print("")
username, password = login(user)
print("")


