# -*- coding: utf-8 -*-
# @author: Richard Wong

import numpy as np
from collections import deque
import server

class dataque(object):
    def __init__(self):
        self.que = deque()
        self.que_len = 0

    def len_out(self):
        if self.que_len == 8:
            return 0
        else:
            return 1

    def ldrop(self):
        self.que.popleft()


    def rpush(self,r_data):
        global time_temp

        data = float(r_data['ticker'])
        if self.que_len == 0:
            self.que.append(data)
            self.que_len += 1
            time_temp = r_data['time']
        else:
            if r_data['time'] != time_temp:
                self.que.append(data)
                self.que_len += 1
                time_temp = r_data['time']
            else:
                pass

    def average(self):
        return np.mean(self.que)

    def average_eight(self,signal):
        data = server.get_data(signal)
        if self.len_out() == 0:
            self.ldrop()
        self.rpush(data)
        return self.average()

#if __name__ == "__main__":
    #d = dataque()
    #for i in range(20):
       # data = server.get_data('btc')
        #if d.len_out() == 0:
           # d.ldrop()
        #d.rpush(data)
        #t = d.average()
        #print(t)
        #print(i)


