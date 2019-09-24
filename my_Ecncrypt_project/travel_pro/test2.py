# from threading import Thread
# import time


# def myfunc(arg1,arg2):
#     print "From thread " + str(arg1)
#     c = arg1 + arg2
# time.sleep(int(arg2))
# print "End of " + str(arg1)
#
#
# tid1 = Thread(target=myfunc, args=(1,10))
#
# tid2 = Thread(target=myfunc, args=(2,15))
# tid1.start()
# tid2.start()
# tid1.join()
# tid2.join()


# def get_details():
#     customer_name = input("Enter name: ")
#     pickup_loc = input("Enter pickup location: ")
#     drop_loc = input("Enter drop location :")
# distance = 30
#     main_code.get_distance(pickup_loc,drop_loc)
# return distance,customer_name
#
# x =  get_details()
# print x[1]


# import threading
# import time
# def controller():
#     thread = threading.Thread(target=fun, args=())
#     thread.daemon = True
# thread.start()
# print_text()
#
# def fun():
#     """ Method that runs forever """
#     print('Doing something imporant in the background ....')
#     time.sleep(10)
#     print("backgroud task is completed")
#
# def print_text():
#     for x in range(5):
#         print 'print_txt '+str(x)
#
# controller()


import threading
# import time

#
# result = None
# result_available = threading.Event()
#
# def background_calculation():

# time.sleep(5)

# global result
# result = 42
# result_available.set()

# time.sleep(6)
#
# def main():
#     thread = threading.Thread(target=background_calculation)
#     thread.start()
#
# result_available.wait()
#
# print('The result is', result)
#
# main()
# lock = threading.Lock()


# def maitain():
#     lock.acquire()
#     print "Start"
#     time.sleep(6)
#     print "End"
#     lock.release()
#
#
# def part2():
#     for x in range(5):
#         print "x : " + str(x)
#
#
# def controller():
#     t1 = threading.Thread(target=maitain)
#     t1.start()
#     part2()
# controller()


from multiprocessing import Process,Lock
import os
import time

# def info(title):
#     print title
#     print 'module name:', __name__
#     if hasattr(os, 'getppid'):  # only available on Unix
#         print 'parent process:', os.getppid()
#     print 'process id:', os.getpid()
#
# def f(name):
#     info('function f')
#     print 'hello', name
#
# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()



# def __init__(self, name):
#     self.name = name


def printing_data(names, locks):
    locks.acquire()
    print "Printing strated "
    time.sleep(5.00)
    print names
    time.sleep(10.00)
    locks.release()


def main_pro(name):
    Process(target=printing_data, args=(name, lock)).start()


if __name__ == '__main__':
    lock = Lock()
    names = ["kranthi","kumar"]

    # for x in names:
        # print x
    Process(target= main_pro, args=(names)).start()





# def f(l, i):
#     l.acquire()
#     print 'hello world', i
#     l.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#
#     for num in range(10):
#         Process(target=f, args=(lock, num)).start()


