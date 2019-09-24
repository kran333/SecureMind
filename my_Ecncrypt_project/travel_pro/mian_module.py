#Author: Kranthi Kumar K
#Date: 23/09/2019

import view_module
import controller_module
import threading, time

class main_controller(object):
    def __init__(self):
        self.option = view_module.menu_details()
        self.control_obj = controller_module.controller_mod()

    def controller(self):
        if self.option == 1:
            det = view_module.get_user_inputs()
            arg = (det[0], det[1], det[2])
            threading.Thread(target=self.control_obj.moniter, args= arg).start()
            time.sleep(2)
            obj = main_controller()
            obj.controller()
        elif self.option == 2:
            cab = view_module.bill_details()
            if cab == "":
                res = self.control_obj.get_total_bill()
            else:
                res = self.control_obj.get_total_bill(cab=cab)
            for a in res:
                for x in a:
                    print "   " + str(x),
                print
            self.controller()
        elif self.option == 3:
            exit()


obj1 = main_controller()
obj1.controller()
