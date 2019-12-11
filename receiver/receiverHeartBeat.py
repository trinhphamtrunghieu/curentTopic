import time
import requests;
import receiver.utils as ut
import receiver.getToken as gt


def listen():
    old = 0
    try:
        while True:
            DEVICE_ID = '8aba4dc0-1a51-11ea-a07b-510cd1df43ec'
            headers = {
                "Content-Type": "application/json",
                "X-Authorization": "Bearer " + ut.token
            }
            url = "http://demo.thingsboard.io/api/plugins/telemetry/DEVICE/" + DEVICE_ID + "/values/timeseries?keys" \
                                                                                           "=value"
            response = requests.get(url, headers=headers);
            #print(response)
            response = response.json()
            if response['value'][0]['ts'] != old:
                print("Heart beat per 5 seconds " + response['value'][0]['value'])
                old = response['value'][0]['ts']
            else:
                old = response['value'][0]['ts']
            time.sleep(2)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    listen()
