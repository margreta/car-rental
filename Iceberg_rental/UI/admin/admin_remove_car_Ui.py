def remove_car():
    
    #Header:
    print("ADMIN/Remove car")
    print("-" *20)

    #Get information from user about the car to be added: 
    again = "y"
    while again == "y":
        license_num = input("Please enter license plate number of car to remove from system: ")
        confirm = input("Are you sure you want to remove {} from system?".format(license_num.upper()))
        
        print("{} has been removed from system".format(license_num.upper()))
        print("")
        
        again = input("Do you want to remove another car? (y/n)")