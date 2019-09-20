import view_module
import controller_module
import threading, time


class main_controller(object):
    def __init__(self):
        pass

    def controller(self):
        option = view_module.menu_details()
        if option == 1:
            det = view_module.get_user_inputs()
            distance = controller_module.get_distance(det[1], det[2])
            threading.Thread(target=controller_module.suspen, args=(distance, det[0])).start()
            time.sleep(2)
            obj = main_controller()
            obj.controller()
        elif option == 2:
            view_module.get_bill()
        elif option == 3:
            exit()


obj1 = main_controller()
obj1.controller()
