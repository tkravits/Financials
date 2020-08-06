import robin_stocks as rh
import json
import pandas as pd

with open(r'credentials.txt') as f:
  data = json.load(f)

login = rh.authentication.login(data)

top_movers = rh.markets.get_top_movers(direction='up')

meme = pd.DataFrame(top_movers)

