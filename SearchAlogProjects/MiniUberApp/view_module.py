#Author: Kranthi Kumar K
#Date: 10/15/2019
import mian_module as mm
import time
def get_user_inputs():
    try:
        customer_id = input("Enter Customer ID : ")
        customer_name = check_user(customer_id)
        pickup_loc = input("Enter pickup location : ")
        drop_loc = input("Enter drop location :")
    except Exception as e:
        print "Invalid Input"
    return customer_id, customer_name, pickup_loc, drop_loc

def menu_details():
    print "1. Bookcab"
    print "2. check all bills"
    print "3. exit"
    option = 0
    try:
        option = int(input("Enter the choice :"))
    except Exception as e:
        pass

    return option

def bill_details():
    print "1. Cab_id : "
    print "2. All Cabs : "
    cab_id = ""
    try:
        choice = int(input("Enter your choice : "))
    except Exception as e:
        pass
    if choice == 1:
        cab_id  = input("Enter Cab ID : ")
    else:
        cab_id = ""
    return cab_id

def check_user(c_id):
    obj = mm.main_controller()
    user_name = obj.check_user(c_id)
    if user_name == "NO":
        print "Invalid User ID.... " +" Please try again."
        time.sleep(2)
        obj.controller()
    else:
        return user_name