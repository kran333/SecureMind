#Author: Kranthi Kumar K
#Date: 10/15/2019
import logging
import view_module
import controller_module
import threading, time
from tabulate import tabulate

logging.basicConfig(filename="travel_log_file.log", format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
class main_controller(object):
    def __init__(self):
        logger.info("Creation of controller_module object in controller_module.py ")
        self.control_obj = controller_module.controller_mod()

    def controller(self):
        logger.info("calling view module's menu details method.")
        self.option = view_module.menu_details()
        if self.option == 1:
            det = view_module.get_user_inputs()
            arg = (det[0], det[1], det[2], det[3])
            threading.Thread(target=self.control_obj.moniter, args=arg).start()
            time.sleep(2)
            obj = main_controller()
            obj.controller()
        elif self.option == 2:
            cab = view_module.bill_details()
            if cab == "":
                res = self.control_obj.get_total_bill()
            else:
                res = self.control_obj.get_total_bill(cab=cab)
            print(tabulate(res, headers='keys', tablefmt='psql'))
            self.controller()
        elif self.option == 3:
            res = self.control_obj.close_control_module()
            if res == True:
                exit()
            else:
                print "Process is running in back end"
        else:
            print "Invalid Option please try again "
            self.controller()
    def check_user(self, cus_id):
       return self.control_obj.check_user_name(cus_id)

if __name__ == '__main__':
    logger.debug("Start of the Program")
    obj1 = main_controller()
    logger.info("calling controller function")
    obj1.controller()