# -*- coding: utf-8 -*-
# @author: Richard Wong

import time
import hashlib
import json
import websocket
import zlib
from threading import Thread

# 账户
api_key = "ad5e2d58-5417-4fdd-921d-2bf9688377d6"
secret_key = "194DD4436BF77CEE167CC10108566E0C"

# 电子货币
BTC = 'btc'
LTC = 'ltc'

# 网站
OKCOIN = 'wss://real.okcoin.com:10440/websocket/okcoinapi'

class OKCoinAPI(object):
    """基于websocket"""

    def __init__(self):
        self.api_key = ''   # 账号
        self.secret_key = ''   # 密码
        self.url = ''    # 服务器
        self.ws = None
        self.thread = None


    ###### tick data ######
    def readData(self,evt):
        try:
            decompress = zlib.decompressobj(-zlib.MAX_WBITS)
            inflated = decompress.decompress(evt) + decompress.flush()

            data = json.loads(inflated)

            return data

        except zlib.error as err:
            data = json.loads(evt)
            return data

    def generateSign(self,params):
        l = []
        for key in sorted(params.keys()):
            l.append('%s=%s' % (key, params[key]))
        l.append('secret_key=%s' % self.secret_key)
        sign = '&'.join(l)
        return hashlib.md5(sign.encode('utf-8')).hexdigest().upper()

    def onMessage(self,ws,evt):
        data = self.readData(evt)
        print(data[0]['channel'],data)

    def onError(self,ws,evt):
        print(evt)

    def onClose(self,ws):
        print('onClose')

    def onOpen(self,ws):
        print('onClose')

    def connect(self,url,apikey,secretkey,trace = False):
        self.url = url
        self.api_key = apikey
        self.secret_key = secretkey

        websocket.enableTrace(trace)

        self.ws = websocket.WebSocketApp(url,
                                         on_message = self.onMessage,
                                         on_error = self.onError,
                                         on_close = self.onClose,
                                         on_open = self.onOpen)

        self.thread = Thread(target=self.ws.run_forever)
        self.thread.start()

    def reconnect(self):
        self.close()

        self.ws = websocket.WebSocketApp(url,
                                         on_message = self.onMessage,
                                         on_error = self.onError,
                                         on_close = self.onClose,
                                         on_open = self.onOpen)

        self.thread = Thread(target=self.ws.run_forever)
        self.thread.start()

    def close(self):
        if self.thread and self.thread.isAlive():
            self.ws.close()
            self.thread.join()

    def sendMarketDataRequest(self,channel):
        """发送交易请求"""

        d = {}
        d['event'] = 'addChannel'
        #d['binary'] = True
        d['channel'] = channel

        j = json.dumps(d)

        try:
            self.ws.send(j)

        except websocket.WebSocketConnectionClosedException:
            pass

    def subscribeTicker(self,symbol):
        self.sendMarketDataRequest('ok_sub_spot_%s_usd_ticker' %symbol)


if __name__ == "__main__":
    api = OKCoinAPI()
    url = OKCOIN
    #api.connect(url, api_key, secret_key, trace=False)

    while 1:
        api.connect(url, api_key, secret_key, trace=False)
        api.subscribeTicker(BTC)
        time.sleep(0.8)