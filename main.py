import os
from threading import Thread
import threading


def sugar():
    os.system("sensor\\sugar.py")


def heat():
    os.system("sensor\\test.py")


def pressure():
    os.system("sensor\\blood.py")


def chol():
    os.system("sensor\\chol.py")

def heart():
    os.system("sensor\\heart.py")

def getValue():
    os.system("receiver\\receiverSugar.py")


t1 = threading.Thread(target=sugar)
t2 = threading.Thread(target=heat)
t3 = threading.Thread(target=pressure)
t4 = threading.Thread(target=chol)
t5 = threading.Thread(target=heart)
t6 = threading.Thread(target=getValue());
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
print("Job done")
