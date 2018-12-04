def homepage():
    """prints the homepage of Iceberg Rental system and prompts for user to choose operator"""
    print("HOME")
    print("-" * 20)
    print("Who are you?")
    print("1. Admin\n2. Dealer\n3. Customer")
    user = input("Please press 1, 2 or 3 to make your pick: ")
    return user