#!/usr/bin/python
import websocket
from parser import parse, terminate, init
import argparse

def init_args():
    parser = argparse.ArgumentParser(description='Gemini MD TUI client')
    parser.add_argument("--sym", type=str, default="BTCUSD", choices=["BTCUSD", "ETHUSD", "ETHBTC"],
                        help="The symbol to subscribe to")
    parser.add_argument("--levels", type=int, default=20, help="How many levels to desplay in the book")
    return parser

if __name__ == '__main__':

    parser = init_args()
    args = parser.parse_args()

    try:
        init(args.levels)
        ws = websocket.WebSocketApp("wss://api.gemini.com/v1/marketdata/" + args.sym, on_message=parse)
        ws.run_forever(ping_interval=5)

    finally:

        terminate()
