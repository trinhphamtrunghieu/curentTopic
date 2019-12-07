import time
import sys
import paho.mqtt.client as mqtt
import json
import random

THINGS_BOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'x7uIppJmEM9BgCvgNgFu'

sensor_sugar_data = {'Value': 0}

minS = 90;
maxS = 150;

client = mqtt.Client()

client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGS_BOARD_HOST,1883)
client.loop_start()
try:
    while True:
            tmp = random.randrange(minS,maxS)
            print('sugar value:{:g}'.format(tmp))
            sensor_sugar_data['tmp'] = tmp;
            client.publish('v1/devices/me/telemetry',json.dumps(sensor_sugar_data))
        
except KeyboardInterrupt:
    pass
client.loop_stop()
client.disconnect()

