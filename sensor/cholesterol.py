import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random

THINGS_BOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'VBg4o7bX447SIQ1TTeiF'

sensor_cholesterol_data = {'value': 0}

maxc = 105
minc = 95

client = mqtt.Client()

client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGS_BOARD_HOST, 1883)
client.loop_start()
try:
    while True:
        value = random.randrange(minc, maxc)
        print(time.ctime() + ': Cholesterol value: {:g}'.format(value))
        sensor_cholesterol_data['valueLow'] = value;
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_cholesterol_data))
        time.sleep(5)

except KeyboardInterrupt:
    pass
client.loop_stop()
client.disconnect()

