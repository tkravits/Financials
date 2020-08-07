import robin_stocks as r
import json
import pandas as pd

with open(r'credentials.txt') as f:
    data = json.load(f)

login = r.authentication.login(data)

top_movers_sp500 = r.markets.get_top_movers_sp500('up')
top_movers_all = r.markets.get_top_movers()

sp500_movers = pd.DataFrame(top_movers_sp500)

meme = pd.DataFrame(top_movers_all)
cols = ['ask_price', 'bid_price', 'last_trade_price', 'last_extended_hours_trade_price', 'previous_close',
        'adjusted_previous_close']
meme[cols] = meme[cols].apply(pd.to_numeric, errors='coerce', axis=1)
meme['Direction Percentage'] = ((meme['last_trade_price'] - meme['previous_close'])
                                / meme['previous_close'])*100
meme = meme[['symbol', 'Direction Percentage', 'ask_price', 'bid_price', 'last_trade_price',
             'last_extended_hours_trade_price', 'previous_close', 'adjusted_previous_close']]
