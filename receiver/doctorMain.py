import os
import receiver.getToken as gt;
import receiver.utils as ut
import receiver.receiverSugar as rS
from threading import Thread
import threading

def getSugarValue():
    rS.listen()


def getBloodValue():
    receiverBlood.listen()

def getCholValue():
    receiverChol.listen()

def getHeartBeat():
    receiverHeartBeat.listen()

def getTemp():
    getTemp().listen()

gt.start()

# t1 = threading.Thread(target=getBloodValue)
# t2 = threading.Thread(target=getSugarValue)
# t3 = threading.Thread(target=getCholValue)
# t4 = threading.Thread(target=getHeartBeat)
# t5 = threading.Thread(target=getTemp)
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
#
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()

print(ut.token)
print("Job done")
