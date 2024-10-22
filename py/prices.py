# Code to create prices.csv
import pandas as pd
import numpy as np
import ccxt
from datetime import datetime, timedelta

coins = ['BTC', 'XRP', 'ETH', 'BCH', 'ADA', 'XEM', 'LTC', 'TRX', 'XLM', 'EOS',
         'NEO', 'ETC', 'LSK', 'DOGE', 'SNT', 'BNB', 'GNT', 'REP']

binance = ccxt.binance()
start = datetime(year=2018,month=1,day=1)
df = pd.DataFrame([])

for coin in coins:
    start_date = start
    ohlcv_coin = []

    if coin == 'BTC':
        ticker = 'BTC/USDT'
    else:
        ticker = coin + '/BTC'

    while start_date < datetime.now():
        data = binance.fetch_ohlcv(ticker, '1h', limit=1000, since=int(start_date.timestamp()*1000))
        ohlcv_coin += data
        start_date += timedelta(hours=len(data))

    close_prices = np.array(ohlcv_coin)[:, 4]
    df[coin] = close_prices
    if coin != 'BTC':
        df[coin] *= df['BTC']


df['date'] = [start + timedelta(hours=i) for i in range(len(df))]
df['date'] = [x.isoformat() for x in df['date']]

# NOTE: indexing is messed up when saved to JSON, so save to CSV
df.to_csv('../prices.csv', index=False)
