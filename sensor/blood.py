import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random
import sensor.utils as ut

THINGS_BOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'YZVBxDMurHfPgeACuATt'

sensor_blood_data = {'valueLow': 0, 'valueHigh': 0}

maxHigh = 190
minHigh = 70
maxLow = 100
minLow = 40

client = mqtt.Client()

client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGS_BOARD_HOST, 1883)
client.loop_start()


def start():
    try:
        while True:
            valueLow = random.randrange(minLow, maxLow)
            valueHigh = random.randrange(minHigh, maxHigh)
            print(time.ctime() + ': blood pressure value: {:g}'.format(valueHigh) + '|{:g}'.format(valueLow))
            if valueLow > valueHigh:
                temp = valueLow
                valueLow = valueHigh
                valueHigh = temp
            ut.bloodLow = valueLow
            ut.bloodHigh = valueHigh
            sensor_blood_data['valueLow'] = valueLow;
            sensor_blood_data['valueHigh'] = valueHigh;
            client.publish('v1/devices/me/telemetry', json.dumps(sensor_blood_data))
            time.sleep(2)

    except KeyboardInterrupt:
        pass
# client.loop_stop()
# client.disconnect()
if __name__ == "__main__":
    start()
