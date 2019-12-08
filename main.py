import os
from threading import Thread
import threading


def sugar():
    os.system("sensor\\sugar.py")

def heat():
    os.system("sensor\\test.py")


t1 = threading.Thread(target=sugar)
t2 = threading.Thread(target=heat)
t1.start()
t2.start()
t1.join()
t2.join()
print("Job done")
