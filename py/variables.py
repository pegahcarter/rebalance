# API token for exchange
token = {
    apiKey: '',
    secret: ''
}

# Coins to rebalance in simulation
COINS = ['BTC', 'ETH', 'XRP', 'LTC', 'XLM']

# Starting dollar value of portfolio simulation
PORTFOLIO_START_VALUE = 5000

# Hour interval to rebalance
INTERVAL = 12

# Column names for transactions.json
COLUMNS = ['date', 'coin', 'side', 'units', 'price_per_unit', 'fees', 'prev_units',
           'cum_units', 'tx_val', 'prev_cost', 'tx_cost',
           'tx_cost_per_unit', 'cum_cost', 'gain_loss', 'realised_pct']

# TODO: fix this file reference
TRANSACTIONS_FILE = '../transactions.json'
