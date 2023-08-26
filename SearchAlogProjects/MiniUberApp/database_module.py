#Author: Kranthi Kumar K
#Date: 10/15/2019

import mysql.connector
import pandas as pd

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="travel_cab_db",
    auth_plugin='mysql_native_password'
)
db_cursor = con.cursor()

class DB_module(object):
    def __init__(self):
        pass

    def get_cab_details(self):
        cab_list = []
        try:
            db_cursor.execute("select cab_id from cab_details")
            res = db_cursor.fetchall()
            for db in res:
                for x in db:
                    cab_list.append(str(x))
            return cab_list
        except Exception as e:
            print e

    def get_avalible_cab(self, loc):
        query1 = "select cab_id,current_location from travel_cab_db.cab_status where c_status = 'F' and current_location = %(curr_loc)s ORDER BY update_timestamp desc limit 1"
        try:
            for x in loc:
                args = {"curr_loc": x}
                df1 = pd.read_sql_query(sql=query1, params=args, con=con)
                return df1
        except Exception as e:
            print e

    def update_fair_details(self, cab_id, cus_id, pickup_loc, drop_loc, distance, price):
        res = False
        try:
            query = """insert into cabs_fair(cab_id,customer_id,pickup_loc,drop_loc,date_of_booking,no_of_km,price) VALUES(%s,%s,%s,%s,now(),%s,%s)"""
            args = (cab_id, cus_id, pickup_loc, drop_loc, distance, price)
            db_cursor.execute(query, args)
            con.commit()
            res = True
        except Exception as e:
            print e
        return res

    def update_cab_curr_status(self, cab_id, curr_state, curr_loc, book_status):
        res = False
        try:
            q1 = """update cab_status set c_status = %(status)s,current_location = %(curr_loc)s,update_timestamp = now(),booking_status = %(book_status)s where cab_id = %(cab_id)s """
            arg = {"status":curr_state,"curr_loc":curr_loc,"cab_id":cab_id, "book_status":book_status}
            db_cursor.execute(q1, arg)
            con.commit()
            res= True
        except Exception as e:
            print str(e)
        return res

    def get_price_from_db(self, cab_id = ''):
        try:
            q1 = """SELECT cf.cab_id as CAB_ID,cf.customer_id as CUSTOMER_ID,cd.customer_name as CUSTOMER_NAME,loc1.location_name as PICK_UP_LOCATION,loc2.location_name as DROP_LOCATION, 
                    cf.date_of_booking as DATE_OF_BOOKING,cf.no_of_km as TOTAL_DISTANCE,cf.price as TOTAL_FAIR
                    from cabs_fair cf inner join customer_details cd on cf.customer_id = cd.customer_id inner join locations loc1 on cf.pickup_loc = loc1.location_code
                    inner join locations loc2 on cf.drop_loc = loc2.location_code ORDER BY cf.cab_id """
            q2 = """SELECT cf.cab_id as CAB_ID,cf.customer_id as CUSTOMER_ID,cd.customer_name as CUSTOMER_NAME,loc1.location_name as PICK_UP_LOCATION,loc2.location_name as DROP_LOCATION, 
                    cf.date_of_booking as DATE_OF_BOOKING,cf.no_of_km as TOTAL_DISTANCE,cf.price as TOTAL_FAIR
                    from cabs_fair cf inner join customer_details cd on cf.customer_id = cd.customer_id inner join locations loc1 on cf.pickup_loc = loc1.location_code
                    inner join locations loc2 on cf.drop_loc = loc2.location_code where cf.cab_id = %(cab_id)s ORDER BY cf.customer_id"""
            if cab_id == '':
                res = pd.read_sql_query(q1,con)
                return res
            else:
                args = {'cab_id':cab_id}
                res = pd.read_sql_query(sql=q2, params=args, con=con)
                return res
        except Exception as e:
            return e

    def close_db_module(self):
        if db_cursor.close() and con.close:
            return True
        else:
            return False
    def get_user_name(self, customer_id):
        try:
            query = " select customer_id,customer_name from customer_details WHERE customer_id = %(c_id)s "
            args = {"c_id": customer_id}
            res = pd.read_sql_query(sql=query, con=con, params=args)
            return res
        except Exception as e:
            return e
    def get_locations(self):
        try:
            query = "SELECT location_code from locations ORDER BY location_code"
            locations = pd.read_sql_query(sql=query,con=con)
            return locations
        except Exception as e:
            return e
    def check_avalible_free_cabs(self):
        query = "SELECT cab_id,current_location from cab_status where c_status = 'F' and booking_status = 'FREE'"
        cabs_dict = {}
        try:
            cabs = pd.read_sql_query(sql=query, con=con)
            for x in range(len(cabs.index)):
                cabs_dict[str(cabs["cab_id"][x])] = str(cabs["current_location"][x])
            return cabs_dict
        except Exception as e:
            return e
    def get_location_distances(self):
        try:
            query = "SELECT * FROM location_distance"
            data = pd.read_sql_query(sql=query, con=con)
            # list = []
            # for x in data.values:
            #     list.append(tuple(x))
            return data
        except Exception as e:
            return e


# obj = DB_module()
# data = obj.get_location_distances()
# string_tuple_list = [tuple(map(str, eachTuple)) for eachTuple in data]
# final_li = []
# for tup in string_tuple_list:
#     li = []
#     for string in tup:
#         if string.isdigit():
#             dig = float(string)
#             print dig
#             li.append(dig)
#         else:
#             li.append(string)
#         t = tuple(li)
#     final_li.append(t)
# print final_li
#