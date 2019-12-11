import time
import requests;
import receiver.utils as ut


def listen():
    old = 0
    try:
        while True:
            DEVICE_ID = '6e45e910-1a51-11ea-bd5a-9f3eedcb469c'
            headers = {
                "Content-Type": "application/json",
                "X-Authorization": "Bearer " + ut.token
            }
            url = "http://demo.thingsboard.io/api/plugins/telemetry/DEVICE/" + DEVICE_ID + "/values/timeseries?keys=valueHigh,valueLow"
            response = requests.get(url, headers=headers).json();
            if(response['value'][0]['ts']!=old):
                print("Cholesterol level "+response['value'][0]['value'])
                old=response['value'][0]['ts']
            else:
                 old=response['value'][0]['ts']
    except KeyboardInterrupt:
        pass