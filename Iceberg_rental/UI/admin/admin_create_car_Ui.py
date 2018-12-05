def create_car(): 
    #Header:
    print("ADMIN/Remove car")
    print("-" *20)
    
    #prompt user for the information about car to create:
    car_type = input("Please enter car type (Type A, Type B, Type C) :")
    license_num = input("Please enter license plate number: ")
    print("")

    confirm = input("Confirm this car registration? (y/n) ")
    print("")
    
    print("The car {} has been added to system.".format(license_num.upper()))
    print("")
    
    again = input("Would you like to add another car? (y/n)")
    return again