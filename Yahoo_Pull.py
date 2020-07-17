import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import talib
import yfinance as yf
from talib import MA_Type

stock = yf.download('QQQ', '2020-1-1','2020-07-07', show_nontrading=True)
#stock['Date'] = stock.index
#stock.index = pd.to_datetime(stock.index)
stock = stock[['Open', 'High', 'Low', 'Close', 'Volume']]

inputs = {
    'open': stock['Open'],
    'high': stock['High'],
    'low': stock['Low'],
    'close': stock['Close'],
    'volume': stock['Volume']
}

close = talib.SMA(stock['Close'])

upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)

output = talib.MOM(close, timeperiod=5)

data = go.Candlestick(x=stock.index,
                open=stock['Open'],
                high=stock['High'],
                low=stock['Low'],
                close=stock['Close'], name='stock OHLC')

# TODO - The BBands are graphing, but they aren't plotting correctly
# TODO - code pulled from https://chart-studio.plotly.com/~jackp/17421/plotly-candlestick-chart-in-python/#/

upper_bb = go.Scatter(x=stock.index, y=upper, name='upper')
lower_bb = go.Scatter(x=stock.index, y=lower, name='lower')
middle_bb = go.Scatter(x=stock.index, y=middle, name='middle')
output = go.Scatter(x=stock.index, y=close)
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(upper_bb, secondary_y=True)
fig.add_trace(lower_bb, secondary_y=True)
fig.add_trace(middle_bb, secondary_y=True)
fig.add_trace(output, secondary_y=True)
fig.add_trace(data, secondary_y=True)

fig.show()