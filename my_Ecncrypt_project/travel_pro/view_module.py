#Author: Kranthi Kumar K
#Date: 23/09/2019

def get_user_inputs():
    customer_name = input("Enter Customer ID : ")
    pickup_loc = input("Enter pickup location : ")
    drop_loc = input("Enter drop location :")
    return customer_name, pickup_loc, drop_loc


def get_bill():
    print "functnality not implemented"
    pass


def menu_details():
    print "1. Bookcab"
    print "2. check all bills"
    print "3. exit"
    option = int(input("Enter the choice :"))
    return option

def bill_details():
    print "1. Cab_id : "
    print "2. All Cabs : "
    cab_id = ""
    choice = int(input("Enter your choice : "))
    if choice == 1:
        cab_id  = input("Enter Cab ID : ")
    else:
        cab_id = ""
    return cab_id
