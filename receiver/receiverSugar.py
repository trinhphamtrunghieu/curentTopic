import os
import time
import sys
import paho.mqtt.client as mqtt
import json
import random

THINGS_BOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'x7uIppJmEM9BgCvgNgFu'

sensor_sugar_data = {'value': 0}

client = mqtt.Client()

client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGS_BOARD_HOST, 1883)
client.loop_start()
client.subscribe("v1/devices/me/telemetry/response/+");
client.publish("v1/devices/me/attributes/request/1");
if client.on_message:
    print("receive message")
client.loop_stop()
client.disconnect()
