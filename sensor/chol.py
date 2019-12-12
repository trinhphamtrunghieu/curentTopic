import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random
import sensor.utils as ut
THINGS_BOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'VBg4o7bX447SIQ1TTeiF'

sensor_cholesterol_data = {'value': 0}

max = 260
min = 180

client = mqtt.Client()

client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGS_BOARD_HOST, 1883)
client.loop_start()
def start():


    try:
        while True:
            value = random.randrange(min, max)
            print(time.ctime() + ': cholesterol value: {:g}'.format(value))
            sensor_cholesterol_data['value'] = value;
            client.publish('v1/devices/me/telemetry', json.dumps(sensor_cholesterol_data))
            ut.cholesterol = value
            time.sleep(2)
            print("\n")
    except KeyboardInterrupt:
        pass
#client.loop_stop()
#client.disconnect()
if __name__ == "__main__":
    start()
