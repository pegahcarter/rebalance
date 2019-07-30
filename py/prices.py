# Code to create prices.csv
import pandas as pd
import numpy as np
import ccxt
from datetime import datetime, timedelta

coins = ['BTC', 'ETH', 'XRP', 'LTC', 'XLM', 'TRX', 'ADA', 'DASH']
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
        data = binance.fetch_ohlcv(ticker, '1h', limit=500, since=int(start_date.timestamp()*1000))
        ohlcv_coin += data
        start_date += timedelta(hours=len(data))

    close_prices = np.array(ohlcv_coin)[:, 4]
    if coin != 'BTC':
        close_prices *= df['BTC']

    df[coin] = close_prices


df['date'] = [start + timedelta(hours=i) for i in range(len(df))]
df.to_csv('src/assets/prices.csv', index=False)
