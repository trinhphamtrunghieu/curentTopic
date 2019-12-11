import time
import requests;
import receiver.utils as ut
import receiver.getToken as gt
old = 0
try:
    if ut.token==" ":
        gt.start()
    while True:
        DEVICE_ID = '4b426100-18da-11ea-a07b-510cd1df43ec'
        headers = {
            "Content-Type": "application/json",
            "X-Authorization": "Bearer " + ut.token
        }
        url = "http://demo.thingsboard.io/api/plugins/telemetry/DEVICE/" + DEVICE_ID + "/values/timeseries?keys=value"
        response = requests.get(url, headers=headers).json();
        print(response)
        if (response['value'][0]['ts'] != old):
            print("Sugar value : " + response['value'][0]['value'])
            old = response['value'][0]['ts']
        else:
            old = response['value'][0]['ts']
except KeyboardInterrupt:
    pass
exit()
