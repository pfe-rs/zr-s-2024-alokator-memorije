from program import *

import threading 
import random
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def funkcija(a, e, sleepTime1, sleepTime2, i):

    # Logovanje početka izvršavanja funkcije
    logging.info("Početak izvršavanja funkcije", i)
    
    time.sleep(sleepTime1)
    c, b = a.algoritam(e)
    
    # Logovanje informacija o rezultatu algoritma
    logging.debug("Rezultat algoritma: c=%s, b=%s", c, b)
    
    # Logovanje trenutnog stanja a.allocated_list i a.memory_list
    logging.debug("Trenutno stanje a.allocated_list: %s", a.allocated_list)
    logging.debug("Trenutno stanje a.memory_list: %s", a.memory_list)
    
    time.sleep(sleepTime2)
    a.deleteElement(i)
    
    # Logovanje nakon brisanja elementa
    logging.debug("Nakon brisanja elementa %s", i)
    logging.debug("------------------")

    # Logovanje kraja izvršavanja funkcije
    logging.info("Kraj izvršavanja funkcije", i)

def main_task(e_list, a):
    a.lock = threading.Lock() 

    thread_list = []
    for i in range(len(e_list)):
        e = Element(e_list[i])
        t = threading.Thread(target = funkcija, args = (a, e, random.random(), random.random(), i))
        thread_list.append(t)
        
        t.start()

    for thread in thread_list:
        thread.join()

if __name__ == "__main__":
    try:
        m = int(input())  # Assuming the first argument is the one you want to convert
    except ValueError:
        print("Error: The argument should be an integer.")
        raise SystemExit

    e_list = []
    for i in range(m):
        try:
            a = list(map(int, input().split())) # Assuming the first argument is the one you want to convert
            e_list.append(a) 
        except ValueError:
            print("Error: The argument should be an list.")
            raise SystemExit
    
    try:
        n = int(input())  # Assuming the first argument is the one you want to convert
    except ValueError:
        print("Error: The argument should be an integer.")
        raise SystemExit
    
    try:
        fit = str(input())  # Assuming the first argument is the one you want to convert
    except ValueError:
        print("Error: The argument should be an string.")
        raise SystemExit
    
    if fit != "FirstFit" and fit != "BestFit":
        print("Error: ovaj algoritam ne posgtoji")

    a = Alokator(n, fit)
    print(a.allocated_list)
    print(a.memory_list)
    print("-------------------------")

    main_task(e_list, a)

    print(a.allocated_list)
    print(a.memory_list)
    print(a.positions_list)


