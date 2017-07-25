import numpy as np

class Book(object):

    def __init__(self, ui, num_level=20):
        """
        ui is the subclass of UI
        num_level is # of level on both side
        """
        self.amount = np.array([], dtype=np.float64)
        self.price = np.array([], dtype=np.float64)
        self.price_dict = {}
        self.sep_idx = 0
        self.reindex = False
        self.ui = ui

    def update_level(self, price, remaining, side):
        """
        Price should be the raw float multiplied by 100 (or 1e8 if ETH/BTC)
        Remaining should be multiplied by 1e8. Basically, properly scaled
        side is 0: bid(buy), 1: ask(sell)
        """
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
                np.delete(self.amount, idx)
                np.delete(self.price, idx)
                self.price_dict.pop(price, None)
                self.reindex = True
                if side == 1:
                    self.sep_idx -= 1


    def finish_update():
        """
        Update the index dictionary and notify the UI
        """
        if self.reindex:
            for i in range(self.price.shape[0]):
                self.price_dict[self.price[i]] = i
        self.ui.update(self.amount, self.price, self.sep_idx)

