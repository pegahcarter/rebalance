import json


class Transactions:

    file = 'transactions.json'

    def __init__(self, simulated, coins):
        try:
            with open(self.file, 'r') as f:
                transactions = json.load(f)
        except:
            transactions = []

        return transactions
