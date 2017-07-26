import json
import numpy as np
from display import TUI
from book import Book

ui = TUI(20)
#ui = None
book = Book(ui)

def parse(ws, message):
    global ui
    global book
    parsed = json.loads(message)
    if parsed["type"] == "update":
        events = parsed["events"]
        for event in events:
            if event["type"] == "change":
#                print(event["price"], event["remaining"], event["side"])
                book.update_level(event["price"], event["remaining"], 0 if event["side"] == "bid" else 1)
        book.finish_update()
