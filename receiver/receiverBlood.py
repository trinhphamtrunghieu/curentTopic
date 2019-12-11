import time
import requests;
import receiver.utils as ut
import receiver.getToken as gt

def listen():
    if ut.token != " ":
        gt.start()

    old = 0
    try:
        while True:
            DEVICE_ID = '44853620-198f-11ea-bd5a-9f3eedcb469c'
            headers = {
                "Content-Type": "application/json",
                "X-Authorization": "Bearer " + ut.token
            }
            url = "http://demo.thingsboard.io/api/plugins/telemetry/DEVICE/" + DEVICE_ID + "/values/timeseries?keys=valueHigh,valueLow"
            response = requests.get(url, headers=headers).json();
            if(response['valueHigh'][0]['ts']!=old):
                print("Current Blood "+response['valueHigh'][0]['value']+"|"+response['valueLow'][0]['value'])
                old=response['valueHigh'][0]['ts']
            else:
                 old=response['valueHigh'][0]['ts']
    except KeyboardInterrupt:
        pass