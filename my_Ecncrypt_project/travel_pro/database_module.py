#Author: Kranthi Kumar K
#Date: 23/09/2019

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
        query2 = "select cab_id,current_location from cab_status where c_status = 'F' ORDER BY update_timestamp limit 1"
        args = {"curr_loc":loc}
        try:
            df1 = pd.read_sql_query(query1, params=args, con=con)
            if df1.empty:
                df2 = pd.read_sql_query(query2, con=con)
                return df2
            else:
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

    def update_cab_curr_status(self, cab_id, curr_state, curr_loc):
        res = False
        try:
            q1 = """update cab_status set c_status = %(status)s,current_location = %(curr_loc)s,update_timestamp = now() where cab_id = %(cab_id)s """
            arg = {"status":curr_state,"curr_loc":curr_loc,"cab_id":cab_id}
            db_cursor.execute(q1, arg)
            con.commit()
            res= True
        except Exception as e:
            print str(e)
        return res

    def get_price_from_db(self, cab_id = ''):
        try:
            q1 = """ select cab_id,customer_id,price from cabs_fair GROUP BY cab_id,customer_id,price ORDER BY cab_id """
            q2 = " select cab_id,customer_id,price from cabs_fair where cab_id = %(cab_id)s GROUP BY cab_id,customer_id,price ORDER BY cab_id "
            if cab_id == '':
                res = pd.read_sql_query(q1,con)
                return res
            else:
                args = {'cab_id':cab_id}
                res = pd.read_sql_query(q2,params=args,con=con)
                return res
        except Exception as e:
            return e

    def close_db_module(self):
        if db_cursor.close() and con.close:
            return True
        else:
            return False