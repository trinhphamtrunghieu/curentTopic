import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random
import sensor.utils as ut

THINGS_BOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'bPrHXMJ0k9681GZG7qCY'

sensor_data = {'temperature': 0}

minTmp = 20;
maxTmp = 40;

client = mqtt.Client()

client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGS_BOARD_HOST, 1883)
client.loop_start()


def start():
    try:
        while True:
            tmp = random.randrange(minTmp, maxTmp)
            print(time.ctime() + ': tmp:{:g}'.format(tmp))
            sensor_data['temperature'] = tmp;
            client.publish('v1/devices/me/telemetry', json.dumps(sensor_data))
            ut.temperature = tmp
            time.sleep(2)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    start()
