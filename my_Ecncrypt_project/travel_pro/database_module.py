import mysql.connector
import view_module
import controller_module

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
        self.data = []

    def get_cab_details(self):
        cab_list = []
        db_cursor.execute("select cab_id from cab_details")
        for db in db_cursor:
            for x in db:
                cab_list.append(str(x))
        return cab_list

    def get_avalible_cab(self, loc):
        avb_cab = ''
        db_cursor.execute("select cab_id from cab_status where c_status = 'F' ORDER BY update_timestamp desc limit 1")
        for db in db_cursor:
            for x in db:
                avb_cab = str(x)
        if avb_cab == '':
            return "false"
        else:
            return avb_cab

    def update_fair_details(self, cab_id):
        basic_det = view_module.get_user_inputs()
        cost = controller_module.get_fair(basic_det[3])
        try:
            query = """insert into cabs_fair(cab_id,customer_id,pickup_loc,drop_loc,date_of_booking,no_of_km,price) VALUES(%s,%s,%s,%s,now(),%s,%s)"""
            args = (cab_id, basic_det[0], basic_det[1], basic_det[2], basic_det[3], cost)
            # args = (cab_id,"1","A","C",30.00,160.00)
            db_cursor.execute(query, args)
            con.commit()
            return True
        except(Exception):
            print Exception
            return False
        finally:
            con.close()

    def update_cab_curr_status(self, cab_id, curr_state):
        try:
            q1 = """update cab_status set c_status = %s,update_timestamp = now() where cab_id = %s """
            tup = (curr_state, cab_id)
            db_cursor.execute(q1, tup)
            con.commit()
            return True
        except Exception as e:
            return e
        finally:
            con.close()
