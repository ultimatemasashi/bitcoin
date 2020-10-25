
from zaifapi import ZaifPublicStreamApi
import time
import subprocess
import requests
import json
import bit3
from zaifapi import ZaifPublicApi;



#print(json_str)


def bitcoin(a) :
             
            time.sleep(50)    
            zaif = ZaifPublicApi();
#print(zaif.last_price("btc_jpy"));
#print(zaif.last_price("btc_jpy"));
            json_str = json.dumps(zaif.last_price("btc_jpy"))
            k = json.loads(json_str)
            print(k['last_price'])
            b = k['last_price']- a
            return b