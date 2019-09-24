#Author: Kranthi Kumar K
#Date: 23/09/2019

import view_module
import controller_module
import threading, time


class main_controller(object):
    def __init__(self):
        self.option = view_module.menu_details()

    def controller(self):
        if self.option == 1:
            det = view_module.get_user_inputs()
            control_obj = controller_module.controller_mod(det[0], det[1], det[2])
            threading.Thread(target=control_obj.suspen).start()
            time.sleep(2)
            obj = main_controller()
            obj.controller()
        elif self.option == 2:
            view_module.get_bill()
        elif self.option == 3:
            exit()


obj1 = main_controller()
obj1.controller()
