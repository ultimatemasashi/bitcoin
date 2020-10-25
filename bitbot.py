from zaifapi import ZaifPublicStreamApi
import time
import subprocess
import requests
import json
import bit3
from zaifapi import ZaifPublicApi;
def send_line_notify(notification_message):
    
    line_notify_token ='**********************'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)
    
    
zaif = ZaifPublicApi();
#print(zaif.last_price("btc_jpy"));

json_str = json.dumps(zaif.last_price("btc_jpy"))
k = json.loads(json_str)


print(k['last_price'])

print(bit3.bitcoin(k['last_price']))

                                  

c = 1
while c == 1  :
 x =  bit3.bitcoin(k['last_price'])   
 
 #send_line_notify(x)   
 if  bit3.bitcoin(k['last_price']) > 500:
            
            #subprocess.check_call(['python3','sall.py'])
            print(x)
            #print('sale bitcoin')
            send_line_notify('上昇')
            send_line_notify(x)
 if   bit3.bitcoin(k['last_price'])  < -500:
            print(x)
            #subprocess.check_call(['python3','buy.py'])
            #print('buy bitcoin')
            send_line_notify('下降')
            send_line_notify(x)
           
