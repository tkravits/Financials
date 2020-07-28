import plotly.graph_objects as go
from plotly.subplots import make_subplots
import talib
from talib import MA_Type
import pandas as pd
import yfinance as yf

# Pull the current date and offset by +1 day to pull the current dataset
CurrentDate = pd.Timestamp.today()
SetDate = (CurrentDate - pd.DateOffset(-1))

# download the historical stock from yahoo finance and set the closing number to np.array
stock = yf.download('QQQ', start='2019-1-1', end=SetDate)
close = stock['Adj Close'].values

# calculate the 50 and 200 day simple moving average for a stock
SMA_50 = talib.SMA(close, timeperiod=50)
SMA_200 = talib.SMA(close, timeperiod=200)

# calculate the bollinger bands
upper, middle, lower = talib.BBANDS(close, matype=MA_Type.T3)

# calculate the relative strength indicator
RSI = talib.RSI(close, timeperiod=14)

# calculate the moving average convergence and divergence
macd, macdsignal, macdhist = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)

# set the plot to make room for 4 charts all in 1 vertical column
fig = make_subplots(rows=4, cols=1)

# sets the plot up graph the stock data in a candlestick format
fig.append_trace(go.Candlestick(x=stock.index,
                open=stock['Open'],
                high=stock['High'],
                low=stock['Low'],
                close=stock['Adj Close'], name='stock OHLC'), row=1, col=1)

# sets the plot up to graph the upper, middle, and lower bbands
upper_bb = go.Scatter(x=stock.index, y=upper, name='upper')
middle_bb = go.Scatter(x=stock.index, y=middle, name='middle')
lower_bb = go.Scatter(x=stock.index, y=lower, name='lower')

# set the plot to graph the 50 day and 200 day simple moving average
SMA_50 = go.Scatter(x=stock.index, y=SMA_50, name='50 Day Simple Moving Average')
SMA_200_chart = go.Scatter(x=stock.index, y=SMA_200, name='200 Day Simple Moving Average')

# adds the created plots to the final plot
fig.add_trace(upper_bb)
fig.add_trace(middle_bb)
fig.add_trace(lower_bb)
fig.add_trace(SMA_50)
fig.add_trace(SMA_200_chart)

# create a new plot that will show the RSI,
fig.append_trace(go.Scatter(x=stock.index, y=RSI, name='RSI'), row=3, col=1)

# formatting the plot
fig.update_layout(height=1200, width=1000, title_text="Indicators")

# display the plot
fig.show()
