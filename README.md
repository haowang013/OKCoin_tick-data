# OKCoin_tick-data
BTC/LTC tick data push service
<br/>
Environment: PyQt5, Python3.6
<br/>
OKCoin offers us two interfaces including websocket and rest. However, the websocket can't be connected. Hence, we use the rest to attain the tick data from the web and then I define a struct based on deque to cache the tick data and calculate the MA8.
<br/>
We use the PyQt5 to design the UI and users could see the tick and MA8 of the LTC and BTC.
The final result as following:
![image](https://github.com/richardwang013/OKCoin_tick_data/raw/master/ImageStore/result.PNG)
