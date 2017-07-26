import numpy as np
import decimal
from threading import Lock

class Book(object):

    def __init__(self, ui):
        """
        ui is the subclass of UI
        """
        self.amount = np.array([], dtype=np.dtype(decimal.Decimal))
        self.price = np.array([], dtype=np.dtype(decimal.Decimal))
        self.price_dict = {}
        self.sep_idx = 0
        self.reindex = False
        self.ui = ui
        self.lock = Lock()
        self.bid = 0
        self.ask = 0

    def update_level(self, price, remaining, side):
        """
        Price should be the raw float multiplied by 100 (or 1e8 if ETH/BTC)
        Remaining should be multiplied by 1e8. Basically, properly scaled
        side is 0: bid(buy), 1: ask(sell)
        """
        if not self.lock.locked():
            self.lock.acquire()
        price = -decimal.Decimal(price)
        remaining = decimal.Decimal(remaining)
        #self.ui.set_status("Processing " + str(price) + " " + str(remaining) + " " + str(side))
        if remaining > 0:
            if price in self.price_dict:
                self.amount[self.price_dict[price]] = remaining
            else:
                idx = np.searchsorted(self.price, price)
                self.amount = np.insert(self.amount, idx, remaining)
                self.price = np.insert(self.price, idx, price)
                self.price_dict[price] = idx
                self.reindex = True
                if side == 1:
                    self.sep_idx += 1
        elif price in self.price_dict:
            idx = self.price_dict[price]
            self.amount = np.delete(self.amount, idx)
            self.price = np.delete(self.price, idx)
            self.price_dict.pop(price, None)
            self.reindex = True
            if side == 1:
                self.sep_idx -= 1


    def finish_update(self):
        """
        Update the index dictionary and notify the UI
        """
        if self.reindex:
            for i in range(self.price.shape[0]):
                self.price_dict[self.price[i]] = i
        self.ui.update(self.amount, -self.price, self.sep_idx)
        self.lock.release()

