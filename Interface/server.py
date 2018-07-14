# -*- coding: utf-8 -*-
# @author: Richard Wong

import json
import urllib.request
import time
from collections import deque


def get_data(signal):
    url = 'https://www.okcoin.com/api/v1/ticker.do?symbol=%s_usd' %signal
    response = urllib.request.urlopen(url,timeout=3)
    data = response.read().decode('utf-8')
    json_data = json.loads(data)
    #print(signal+': '+json_data['date']+': '+json_data['ticker']['last'])
    rural_data = {'time':json_data['date'],'ticker':json_data['ticker']['last']}
    return rural_data

#if __name__ == "__main__":
    #while True:
        #tasks = ['btc','ltc']
        #for ta in tasks:
            #task = threading.Thread(target=get_data,args=(ta,))
            #task.start()
            #print()
        #time.sleep(1)
    #arr = deque([])
    #for i in range(10):
        #x = a(i,arr)
        #print(x)
    #ar = deque([])
    #for j in range(10,25):
       # y = a(j,ar)
       # print(y)
#if __name__ == "__main__":
    #while 1:
        #t = get_data('btc')
        #print(t)