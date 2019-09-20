import time, threading
from travel_pro import database_module

lock = threading.Lock()


class controller_module(object):
    def __init__(self):
        pass

    def suspen(self, distance, cus_name):
        lock.acquire()
        speed = 80.00 / 3.6
        distance = distance * 1000
        sus_time = (distance / speed) / 100
        print cus_name + " your cab is Booked," + "it takes " + str(sus_time) + " sec. to reach the destination"
        time.sleep(int(sus_time))
        lock.release()

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
        return c * distance

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

    def get_cab(self):
        cab_list = database_module.get_cab_details()
        cab_status = "F"
        return cab_list[0]

    def check_cab_avaliability(self, curr_loc):
        db_obj = database_module()
        cab_num = db_obj.get_avalible_cab(curr_loc)
        return cab_num


obj = controller_module()
print obj.check_cab_avaliability("A")
# print obj.get_cab()