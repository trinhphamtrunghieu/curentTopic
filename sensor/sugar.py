import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random
import sensor.utils as ut

THINGS_BOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'x7uIppJmEM9BgCvgNgFu'

sensor_sugar_data = {'value': 0}

minS = 50;
maxS = 200;

client = mqtt.Client()

client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGS_BOARD_HOST, 1883)
client.loop_start()


def start():
    try:
        while True:
            tmp = random.randrange(minS, maxS)
            print(time.ctime() + ': sugar value:{:g}'.format(tmp))
            sensor_sugar_data['value'] = tmp;
            client.publish('v1/devices/me/telemetry', json.dumps(sensor_sugar_data))
            ut.sugar = tmp
            time.sleep(2)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    start()
