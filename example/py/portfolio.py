

class Portfolio:

    def __init__(self, coins=None):

        if coins is None:
            coins = ???

        self.transactions = Transactions
        self.exchange = Exchange
        self.summary = Summary
        self.coins = {Coin(coin) for coin in coins}


    def update(self):
        update_summary()
        update_exchange()
        update_transactions()
        update_coins()


    def update_summary(Summary):
        pass


    def update_exchange(Exchange):
        pass


    def update_transactions(Transactions):
        pass


    def update_coins(Coins):
        pass
