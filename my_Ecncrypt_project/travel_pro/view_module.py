def get_user_inputs():
    customer_name = input("Enter name: ")
    pickup_loc = input("Enter pickup location: ")
    drop_loc = input("Enter drop location :")
    return customer_name, pickup_loc, drop_loc


def get_bill():
    print "functnality not implemented"
    pass


def menu_details():
    print "1. Bookcab"
    print "2. check the bill"
    print "3. exit"
    option = int(input("Enter the choice :"))
    return option
