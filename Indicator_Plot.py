import plotly.graph_objects as go
from plotly.subplots import make_subplots
import talib
from talib import MA_Type
import yfinance as yf

stock = yf.download('QQQ', start='2019-1-1', end='2020-07-22')

SMA = talib.SMA(stock['Adj Close'].values, timeperiod=50)
SMA_200 = talib.SMA(stock['Adj Close'].values, timeperiod=200)

upper, middle, lower = talib.BBANDS(stock['Adj Close'], matype=MA_Type.T3)

data = go.Candlestick(x=stock.index,
                open=stock['Open'],
                high=stock['High'],
                low=stock['Low'],
                close=stock['Adj Close'], name='stock OHLC')


upper_bb = go.Scatter(x=stock.index, y=upper, name='upper')
lower_bb = go.Scatter(x=stock.index, y=lower, name='lower')
middle_bb = go.Scatter(x=stock.index, y=middle, name='middle')
output = go.Scatter(x=stock.index, y=SMA, name='50 Day Simple Moving Average')
SMA_200_chart = go.Scatter(x=stock.index, y=SMA_200, name='200 Day Simple Moving Average')
fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(upper_bb, secondary_y=True)
fig.add_trace(lower_bb, secondary_y=True)
fig.add_trace(middle_bb, secondary_y=True)
fig.add_trace(output, secondary_y=True)
fig.add_trace(SMA_200_chart, secondary_y=True)
fig.add_trace(data, secondary_y=True)

fig.show()