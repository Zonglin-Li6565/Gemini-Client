from abc import ABC, abstractmethod

class UI(ABC):
    @abstractmethod
    def update(amount, price, seq_idx):
        pass

class TUI(UI):

    def __init__(self, n_levels):
        curses.initscr()
        self.n_levels = n_levels

    def close(self):
        curses.endwin()

    def update(amount, price, seq_idx):
        
