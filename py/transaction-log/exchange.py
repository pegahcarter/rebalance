import ccxt
import pandas as pd
import transactions

api = ccxt.binance()

def fetch_price(coin, date=None):
	''' Return the current dollar price of the coin in question '''

	if coin == 'USDT':
		return 1.0
	else:
		return float(api.fetch_ticker(coin + '/USDT')['info']['lastPrice'])
