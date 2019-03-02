import os
import sys
import pandas as pd
import numpy as np
from datetime import datetime


class Coin(object):

    def __init__(self, coin, price=None):
        self.coin = coin
        self.init_price = None
        self.init_units = None
        self.current_price = None # TODO: add difference between simulation price/current price
        self.current_units = None
        self.market_val = None
        self.transactions = {}
        self.fees = None


    def update_market_val(self):
        pass


    def transact(self, side, units, price):
        if side == 'buy':

        # side == 'sold'
        else:
