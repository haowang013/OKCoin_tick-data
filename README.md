# OKCoin_tick-data
BTC/LTC tick data push service
Environment: PyQt5, Python3.6
OKCoin offers us two interfaces including websocket and rest. However, the websocket can't be connected. Hence, we use the rest to attain the tick data from the web and then I define a struct based on deque to cache the tick data and calculate the MA8.
We use the PyQt5 to design the UI and users could see the tick and MA8 of the LTC and BTC.
