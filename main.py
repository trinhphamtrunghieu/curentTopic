import ctypes
import os
import sys

import receiver.getToken as gt;
import receiver.utils as ut
from receiver import receiverSugar, receiverBlood, receiverChol, receiverHeartBeat
from threading import Thread
import threading
import sensor.chol as sC
import sensor.sugar as sS
import sensor.heart as sH
import sensor.blood as sB
import sensor.test as sT


def sugar():
    sS.start()


def heat():
    sT.start()


def pressure():
    sB.start()


def chol():
    sC.start()


def heart():
    sH.start()


def start():
    t1 = threading.Thread(target=sugar)
    t2 = threading.Thread(target=heat)
    t3 = threading.Thread(target=pressure)
    t4 = threading.Thread(target=chol)
    t5 = threading.Thread(target=heart)

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
    print("Job done")

def stop():
    sys.exit()

if __name__ == "__main__":
    start()
