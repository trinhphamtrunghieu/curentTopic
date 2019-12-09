import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random

THINGS_BOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'ljYfx6gZ90rI3JjgKeEM'

sensor_cholesterol_data = {'value': 0}

maxc = 105
minc = 55

client = mqtt.Client()

client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGS_BOARD_HOST, 1883)
client.loop_start()
try:
    while True:
        value = random.randrange(minc, maxc)
        print(time.ctime() + ': Heartbeat value: {:g}'.format(value))
        sensor_heartbeat_data['value'] = value;
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_heartbeat_data))
        time.sleep(5)

except KeyboardInterrupt:
    pass
client.loop_stop()
client.disconnect()

