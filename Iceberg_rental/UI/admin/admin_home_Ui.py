from getpass import getpass

from Ui.admin.admin_create_car_Ui import create_car

def admin():
    """interface that admin can access"""
    
    #Header: 
    print("ADMIN/Create new car")
    print("-" *20)

    #prompt for action from user: 
    print("Choose action: ")
    choice = getpass("1. Create new car\n2. Remove car\n3. Mark car for repair\n4. Go back\n ")
    print("")


    #Go to relevant "page":
    if choice == "1":
        create_car()
    # elif choice == "2":
    #     remove_car()
    # elif choice == "3":
    #     mark_repair
    # elif choice == "4":
    #     pass