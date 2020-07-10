import talib as ta
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('bmh')
import yfinance as yf
stock = yf.download('TLRY', '2020-1-1','2020-07-07')
inputs = {
    'open': stock['Open'],
    'high': stock['High'],
    'low': stock['Low'],
    'close': stock['Adj Close'],
    'volume': stock['Volume']
}
from talib import abstract

# directly
SMA = abstract.SMA

# or by name
SMA = abstract.Function('sma')

from talib.abstract import *
# uses close prices (default)
output = SMA(inputs, timeperiod=25)

# uses open prices
output = SMA(inputs, timeperiod=25, price='open')

# uses close prices (default)
upper, middle, lower = BBANDS(inputs, 20, 2, 2)

# uses high, low, close (default)
slowk, slowd = STOCH(inputs, 5, 3, 0, 3, 0) # uses high, low, close by default

# uses high, low, open instead
slowk, slowd = STOCH(inputs, 5, 3, 0, 3, 0, prices=['high', 'low', 'open'])



# #output = ta.MOM(inputs, timeperiod=5)
# indicator_1 = 'RSI'
# stock[indicator_1] = ta.SMA(stock['Close'],14)
# stock['MACD'] = ta.EMA(stock['Close'], timeperiod = 14)
# # Plot
# stock[['Close',SMA,'MACD']].plot(figsize=(15,15))
# plt.show()