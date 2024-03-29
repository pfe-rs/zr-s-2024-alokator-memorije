from program import *

import threading 
import random
import time



def main_task(e_list, a):
    a.lock = threading.Lock() 

    thread_list = []
    for i in range(len(e_list)):
        e = Element(e_list[i])
        t = threading.Thread(target = a.algoritam, args = (e, ))
        thread_list.append(t)
        print("i =", i)
        t.start()

    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    e_list = [[3, 4], [5, 6], [7, 8, 9], [0, 1, 2]]
    n = 20
    fit = "FirstFit"

    a = Alokator(n, fit)
    print(a.allocated_list)
    print(a.memory_list)
    print("-------------------------")

    main_task(e_list, a)

    print(a.allocated_list)
    print(a.memory_list)
    print(a.positions_list)


