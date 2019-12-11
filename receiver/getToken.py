import time
import json

import requests;
import receiver.utils as ut

def start():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    data = '{"username":"tpth161997@gmail.com", "password":"123456789"}'
    response = requests.post('http://demo.thingsboard.io/api/auth/login', headers=headers, data=data).json();
    ut.token = response['token']
    print(ut.token)
