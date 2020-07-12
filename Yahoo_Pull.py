import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
import talib
import yfinance as yf

stock = yf.download('TLRY', '2020-1-1','2020-07-07')
stock['Date'] = stock.index
stock['Date'] = pd.to_datetime(stock['Date'], format='%Y-%m-%d')
stock = stock[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
#stock.set_index('Date', inplace=True, drop=True)

inputs = {
    'open': stock['Open'],
    'high': stock['High'],
    'low': stock['Low'],
    'close': stock['Adj Close'],
    'volume': stock['Volume']
}

close = talib.SMA(stock['Adj Close'])

from talib import MA_Type

upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)

output = talib.MOM(close, timeperiod=5)

mpf.plot(stock[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']])
# TODO - plotting error occurs, it's looking for a datetime column, but the datetime is set as a index, not a column
plt.plot(upper)
plt.plot(middle)
plt.plot(lower)
plt.show()