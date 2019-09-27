#Author: Kranthi Kumar K
#Date: 23/09/2019

import time, threading
import database_module as db
lock = threading.Lock()


class controller_mod(object):
    def __init__(self):
        self.db_obj = db.DB_module()

    def moniter(self, customer_name, pickup_point, drop_point):
        self.customer_name = customer_name
        self.pickup_point = pickup_point
        self.drop_point = drop_point
        self.cab_num = self.check_cab_avaliability()
        if self.cab_num == False:
            print "NO cabs are avalible in your location...!"
            exit()
        else:
            self.distance = self.get_distance(self.pickup_point, self.drop_point)
            self.total_fair = self.get_fair(self.distance)
            self.suspen()
    def get_suspend_time(self, distance):
        speed = 80.00 / 3.6
        distance = distance * 1000
        sus_time = (distance / speed) / 10
        return sus_time
    def suspen(self):
        # lock.acquire()
        sus_time = self.get_suspend_time(self.distance)
        self.update_cab_status(cab_num=self.cab_num, status="R", loc=self.pickup_point)
        print str(self.customer_name) + " your cab is Booked,"+" cab number = "+str(self.cab_num)+" it takes " + str(sus_time)+ " sec. to reach the destination"
        time.sleep(int(sus_time))
        self.update_fair_details()
        self.update_cab_status(cab_num=self.cab_num, status="F", loc=self.drop_point)
        # lock.release()

    def get_distance(self, start_point, end_point):
        distance = 15
        a, b, c = 0, 0, 0
        locations = ["A", "B", "C", "D"]
        for x in range(len(locations)):
            if start_point.upper() == locations[x]:
                a = x
            elif end_point.upper() == locations[x]:
                b = x
            else:
                pass
        if a < b:
            c = b - a
        elif b < a:
            c = a - b
        else:
            pass
        dis = c * distance
        return dis

    def get_fair(self, total_distance_traveled):
        base_fair_per_5km = 100.00
        min_distance = 5
        base_fair = 10.00
        total_fair = 0.00
        if total_distance_traveled > min_distance:
            total_fair = base_fair_per_5km
            extra_distance = total_distance_traveled - min_distance
            extra_distance = extra_distance / 2
            print extra_distance
            total_fair = total_fair + extra_distance * base_fair
        return total_fair

    def get_total_bill(self, cab= ""):
        bill = self.db_obj.get_price_from_db(cab_id=cab)
        return bill

    def check_cab_avaliability(self):
        res = self.db_obj.get_avalible_cab(self.pickup_point)
        if res.empty:
            return False
        else:
            if str(res['current_location'][0]) == self.pickup_point:
                return str(res['cab_id'][0])
            else:
                cab_dis = self.get_distance(str(res['current_location'][0]),self.pickup_point)
                wait_time = self.get_suspend_time(cab_dis)
                print self.customer_name + " your cab will be arriving soon in " + str(wait_time) + " Sec.."
                time.sleep(float(wait_time+2))
                self.update_cab_status(cab_num= str(res['cab_id'][0]), status='F', loc=self.pickup_point)
                return self.check_cab_avaliability()
    def update_cab_status(self, cab_num, status, loc):
        res = self.db_obj.update_cab_curr_status(cab_num, status,loc)
        return res

    def update_fair_details(self):
        res = self.db_obj.update_fair_details(self.cab_num,self.customer_name,self.pickup_point,self.drop_point,self.distance,self.total_fair)
        return res

    def close_control_module(self):
        return self.db_obj.close_db_module()


