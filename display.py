from abc import ABC, abstractmethod
import curses

LEFT = 20
TOP  = 1

class UI(ABC):
    @abstractmethod
    def update(self, amount, price, sep_idx):
        pass

    @abstractmethod
    def set_status(self, string):
        pass

class TUI(UI):

    def __init__(self, n_levels):
        self.scr = curses.initscr()
        self.n_levels = n_levels

    def close(self):
        self.scr.erase()
        curses.endwin()

    def set_status(self, string):
        self.scr.addstr(TOP, LEFT, string)
        self.scr.refresh()

    def update(self, amount, price, sep_idx):
        if amount.shape[0] <= 0 or amount.shape[0] != price.shape[0]:
            return

        # draw ask
        for i in range(min(sep_idx, self.n_levels)):
            self.scr.addstr(self.n_levels - i + TOP + 1, 15 + LEFT, " " * 15)
            self.scr.addstr(self.n_levels - i + TOP + 1, 30 + LEFT, " " * 15)
            self.scr.addstr(self.n_levels - i + TOP + 1, 15 + LEFT, str(price[sep_idx - i - 1]))   # add price
            self.scr.addstr(self.n_levels - i + TOP + 1, 30 + LEFT, str(amount[sep_idx - i - 1]))  # add amount

        self.scr.addstr(self.n_levels + TOP + 2, 15 + LEFT, "Spread: " + str(price[sep_idx - 1] - price[sep_idx]))

        # draw bid
        for i in range(min(amount.shape[0] - sep_idx, self.n_levels)):
            self.scr.addstr(2 + self.n_levels + i + TOP + 1, LEFT, " " * 15)
            self.scr.addstr(2 + self.n_levels + i + TOP + 1, 15 + LEFT, " " * 15)
            self.scr.addstr(2 + self.n_levels + i + TOP + 1, LEFT, str(amount[sep_idx + i]))          # add amount
            self.scr.addstr(2 + self.n_levels + i + TOP + 1, 15 + LEFT, str(price[sep_idx + i]))           # add price

        self.scr.refresh()
