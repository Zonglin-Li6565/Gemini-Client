import json
import numpy as np
from display import TUI
from book import Book

ui = None
book = None

def init(levels=20):
    global ui
    global book
    ui = TUI(levels)
    book = Book(ui)
    return ui, book

def parse(ws, message):
    global ui
    global book
    parsed = json.loads(message)
    if parsed["type"] == "update":
        events = parsed["events"]
        for event in events:
            if event["type"] == "change":
                book.update_level(event["price"], event["remaining"], 0 if event["side"] == "bid" else 1)
        book.finish_update()

def terminate():
    if ui != None:
        ui.close()
