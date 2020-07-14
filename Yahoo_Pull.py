import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly
import talib
import yfinance as yf
from talib import MA_Type

stock = yf.download('TLRY', '2020-1-1','2020-07-07')
stock['Date'] = stock.index
stock.index = pd.to_datetime(stock.index)
stock = stock[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

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

data = go.Figure(data=[go.Candlestick(x=stock['Date'],
                open=stock['Open'],
                high=stock['High'],
                low=stock['Low'],
                close=stock['Close'])])
# TODO - The data plots as a real slick candlestick chart, but now I need to figure out how to get BBands
# TODO - and the SMA to overlay over the candlestick chart, lines 36 through 58 need to be worked out
# TODO - code pulled from https://chart-studio.plotly.com/~jackp/17421/plotly-candlestick-chart-in-python/#/
layout = dict()

fig = dict( data=data, layout=layout )

def bbands(price, window_size=10, num_of_std=5):
    rolling_mean = price.rolling(window=window_size).mean()
    rolling_std  = price.rolling(window=window_size).std()
    upper_band = rolling_mean + (rolling_std*num_of_std)
    lower_band = rolling_mean - (rolling_std*num_of_std)
    return rolling_mean, upper_band, lower_band

bb_avg, bb_upper, bb_lower = bbands(stock.Close)

fig['data'].append( dict( x=stock.index, y=bb_upper, type='scatter', yaxis='y2',
                         line = dict( width = 1 ),
                         marker=dict(color='#ccc'), hoverinfo='none',
                         legendgroup='Bollinger Bands', name='Bollinger Bands') )

fig['data'].append( dict( x=stock.index, y=bb_lower, type='scatter', yaxis='y2',
                         line = dict( width = 1 ),
                         marker=dict(color='#ccc'), hoverinfo='none',
                         legendgroup='Bollinger Bands', showlegend=False ) )

fig.show()
#mpf.plot(stock)
# TODO - plotting error occurs, it's looking for a datetime column, but the datetime is set as a index, not a column
fig.append_trace(upper)
plt.plot(upper)
plt.plot(middle)
plt.plot(lower)
plt.show()