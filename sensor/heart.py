import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random
import datetime as dt
import sensor.utils as ut

THINGS_BOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'ljYfx6gZ90rI3JjgKeEM'

sensor_heart_data = {'value': 0, 'sex': 'F', 'age': 0, 'hour': 0}
minS = 50;
maxS = 200;
age = 21
sex = 'M'

client = mqtt.Client()

client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGS_BOARD_HOST, 1883)
client.loop_start()


def start():


    try:
        while True:
            tmp = random.randrange(minS, maxS)
            print(time.ctime() + ': Heartbeat value:{:g}'.format(tmp))
            sensor_heart_data['value'] = tmp;
            sensor_heart_data['age'] = age
            sensor_heart_data['sex'] = sex
            sensor_heart_data['time'] = (dt.datetime.now()).time().hour
            ut.heart = tmp
            client.publish('v1/devices/me/telemetry', json.dumps(sensor_heart_data))
            time.sleep(2)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    start()