# API token for exchange
token = {
    'apiKey': '',
    'secret': ''
}

# Coins to rebalance in simulation
COINS = ['BTC', 'ETH', 'XRP', 'LTC', 'XLM']

# Fee rate per transaction
FEE_RATE = 0.00075

# Difference between market price and order price
SLIPPAGE = 0.005

# Starting dollar value of portfolio simulation
PORTFOLIO_START_VALUE = 5000

# Hour interval to rebalance
INTERVAL = 12

# Column names for transactions.json
COLUMNS = [
    'date',
    'coin',
    'side',
    # 'price',
    'units',
    'cost',
    'prev_units',
    'cum_units',
    'prev_cost',
    'cum_cost',
    'fees'
    # 'cost_per_unit',
    # 'pnl_realised_d_amt',
    # 'pnl_realised_pct',
    # 'pnl_unrealised_d_amt'
]

TRANSACTIONS_FILE = 'src/assets/transactions.json'
SUMMARY_FILE = 'src/assets/summary.json'
