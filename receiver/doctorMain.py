import os
import receiver.getToken as gt;
import receiver.utils as ut
import receiver.receiverSugar as rS
import receiver.receiverBlood as rB
import receiver.receiverChol as rC
import receiver.getTemp as rT
import receiver.receiverHeartBeat as rH
from threading import Thread
import threading


def getSugarValue():
    rS.listen()


def getBloodValue():
    rB.listen()


def getCholValue():
    rC.listen()


def getHeartBeat():
    rH.listen()


def getTemp():
    rT.listen()


def start():
        gt.start()

        t1 = threading.Thread(target=getBloodValue,daemon=True)
        t2 = threading.Thread(target=getSugarValue,daemon=True)
        t3 = threading.Thread(target=getCholValue,daemon=True)
        t4 = threading.Thread(target=getHeartBeat,daemon=True)
        t5 = threading.Thread(target=getTemp,daemon=True)

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

if __name__ == "__main__":
    start()
