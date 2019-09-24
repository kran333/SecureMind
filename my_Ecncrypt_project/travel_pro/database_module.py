#Author: Kranthi Kumar K
#Date: 23/09/2019

import mysql.connector

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
        # finally:
        #     db_cursor.close()
        #     con.close()


    def get_avalible_cab(self, loc):
        avb_cab = ''
        try:
            db_cursor.execute(
                "select cab_id from cab_status where c_status = 'F' ORDER BY update_timestamp limit 1")
            res = db_cursor.fetchall()
            for db in res:
                for x in db:
                    avb_cab = str(x)
            if avb_cab == '':
                return "false"
            else:
                return avb_cab
        except Exception as e:
            print e
        # finally:
        #     db_cursor.close()
        #     con.close()


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
        # finally:
        #     db_cursor.close()
        #     con.close()
        return res

    def update_cab_curr_status(self, cab_id, curr_state):
        res = False
        try:
            q1 = """update cab_status set c_status = %s,update_timestamp = now() where cab_id = %s """
            arg = (curr_state, cab_id)
            db_cursor.execute(q1, arg)
            con.commit()
            res= True
        except Exception as e:
            print str(e)
        # finally:
        #     db_cursor.close()
        #     con.close()
        return res

# obj = DB_module()
# print obj.update_cab_curr_status("cab-3","F")
# print obj.update_fair_details("cab-1","ram","A","C",16.00,160.00)