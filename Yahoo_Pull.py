import plotly.graph_objects as go
from plotly.subplots import make_subplots
import talib
from talib import MA_Type
import yfinance as yf

stock = yf.download('QQQ', '2020-1-1','2020-07-21', show_nontrading=True)

stock = stock[['Open', 'High', 'Low', 'Adj Close', 'Volume']]

stock = stock.iloc[::-1]
stock = stock.dropna()
close = stock['Adj Close']
#close = talib.SMA(stock['Adj Close'].values)
upper, middle, lower = talib.BBANDS(close, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)

output = talib.MOM(close, timeperiod=10)

data = go.Candlestick(x=stock.index,
                open=stock['Open'],
                high=stock['High'],
                low=stock['Low'],
                close=stock['Adj Close'], name='stock OHLC')

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