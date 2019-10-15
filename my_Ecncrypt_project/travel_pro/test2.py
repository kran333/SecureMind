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


# import threading
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


# from multiprocessing import Process,Lock
# import os
# import time

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


# def printing_data(names, locks):
#     locks.acquire()
#     print "Printing strated "
#     time.sleep(5.00)
#     print names
#     time.sleep(10.00)
#     locks.release()
#
#
# def main_pro(name):
#     Process(target=printing_data, args=(name, lock)).start()
#
#
# if __name__ == '__main__':
#     lock = Lock()
#     names = ["kranthi","kumar"]
#
#     for x in names:
#         print x
    # Process(target= main_pro, args=(names)).start()
#
#
#
#

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

# dict = {"A":10,"B":5,"c":8,'d':8}
# li = []
# for value in dict.values():
#     li.append(value)
# li = sorted(li)
# dict_min ={}
# for key, value in dict.items():
#     if li[0] == value:
#         dict_min[key] = value
# print dict_min
# val = ""
# for key, value in dict.items():
#     if value == 5:
#         print type(key)
#         val = str(key)
# print val



# def sum(x, y):
#   """Returns arg1 value add to arg2 value."""
#   return x+y
#   return sum.__doc__
#
# print sum(10, 7)
# def one():
#   return "one function is executed"
#
# def two():
#   return "two function is executed"
#
# def swithch_case(arg):
#   switch = {
#     1:one,
#     2:two
#   }
#   fun = switch.get(arg,lambda :"invalid")
#   return fun()
#
# print swithch_case(3)


# x= 17
# y = 15
# print "x is greater" if x > y else "y is greater"

# def makeSqure(n):
#   i = 1
#   while i < n:
#       yield i * i
#       i += 1
# print(list(makeSqure(5)))
# print makeSqure(5)

# string = ''
# with open('data') as f:
    # string = f.readlines()
# data_list = []
# for x in string:
#     y = ''
#     y = (x.replace(',',"")).lower()
#     data_list.append(y)
# for x in data_list:
#     lis = x.split(" ")
#     print lis.count('the')

# with open('data', 'a') as f:
#     f.write("hello kranthi.....\n")
#     f.write('welcome')
# with open('data','r') as rd:
#     data = rd.read()
#     print data

# def one():
#     return "One function is executing"
# def two():
#     return "two function is executing"
# def choice_function(args):
#     switch = {
#         1:one,
#         2:two
#     }
#     fun =  switch.get(args, lambda : "Invalid Option")
#     return fun()
# print choice_function(3)

# import multiprocessing
# print multiprocessing.cpu_count()


# import py_compile
# py_compile.compile('test2.py')
# import sys
# sys.dont_write_bytecode = True
# import copy
# color1 = ['Red', 'Blue']
# color2 = ['White','Black']
# color3 = [color1 , color2]
# normal copy
# color4 = color3
# print (id(color3) == id(color4))        # True - color3 is the same object as color4
# print (id(color3[0]) == id(color4[0]))  # True - color4[0] is the same object as color3[0]

# shallow copy
# color4 = copy.copy(color3)
# print (id(color3) == id(color4))        # False - color4 is now a new object
# print (id(color3[0]) == id(color4[0]))  # True - The new variable refers to the original variable.

# deep  copy
# color4 = copy.deepcopy(color3)
# print (id(color3) == id(color4))        # False - color4 is now a new object
# print (id(color3[0]) == id(color4[0]))  # False - color4[0] is now a new object


# def get_values(address):
#     try:
#         name = input("Enter the name: ")
#         age = int(input("Enter age : "))
#         return name, age
#     except Exception as e:
#         return
#         pass



