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

# set the plot to make room for all charts all in 1 vertical column, make sure to set
# vertical_spacing to some number 0-0.10 divided by the number of rows
fig = make_subplots(rows=4, cols=1, vertical_spacing=0.10/6)

# sets the plot up graph the stock data in a candlestick format
fig.append_trace(go.Candlestick(x=stock.index,
                open=stock['Open'],
                high=stock['High'],
                low=stock['Low'],
                close=stock['Adj Close'], name='stock OHLC'), row=1, col=1)

# sets the plot up to graph the upper, middle, and lower bbands
upper_bb = go.Scatter(x=stock.index, y=upper, name='Upper BB')
middle_bb = go.Scatter(x=stock.index, y=middle, name='Middle BB')
lower_bb = go.Scatter(x=stock.index, y=lower, name='Lower BB')

# set the plot to graph the 50 day and 200 day simple moving average
SMA_50 = go.Scatter(x=stock.index, y=SMA_50, name='50 Day Simple Moving Average')
SMA_200_chart = go.Scatter(x=stock.index, y=SMA_200, name='200 Day Simple Moving Average')

# adds the created plots to the final plot
fig.add_trace(go.Bar(x=stock.index, y=stock['Volume'], name='Volume'), row=2, col=1)
fig.add_trace(upper_bb)
fig.add_trace(middle_bb)
fig.add_trace(lower_bb)
fig.add_trace(SMA_50)
fig.add_trace(SMA_200_chart)

# create a new plot that will show the RSI,
fig.append_trace(go.Scatter(x=stock.index, y=RSI, name='RSI'), row=3, col=1)

# create a new plot that will display the MACD history as a bar plot, then add the MACD and signal
fig.append_trace(go.Bar(x=stock.index, y=macdhist, name='MACD History'), row=4, col=1)
fig.add_trace(go.Scatter(x=stock.index, y=macd, name='MACD'), row=4, col=1)
fig.add_trace(go.Scatter(x=stock.index, y=macdsignal, name='MACD Signal'), row=4, col=1)

# formatting the plot
fig.update_layout(width=1400, height=2750,
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=7,
                     label='1w',
                     step='day',
                     stepmode='backward'),
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=False
        ),
        type="date"
        )
)
# display the plot
fig.show()
