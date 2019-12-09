import os
from threading import Thread
import threading


def sugar():
    os.system("sensor\\sugar.py")


def heat():
    os.system("sensor\\test.py")


def pressure():
    os.system("sensor\\blood.py")

def cholesterol():
    os.system("senssor\\cholesterol.py")


t1 = threading.Thread(target=sugar)
t2 = threading.Thread(target=heat)
t3 = threading.Thread(target=pressure)
t4 = threading.Thread(target=cholesterol)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print("Job done")
