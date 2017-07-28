#!/usr/bin/python
import websocket
from parser import parse, terminate, init
import argparse
import sys

def init_args():
    parser = argparse.ArgumentParser(description='Gemini MD TUI client')
    parser.add_argument("--sym", type=str, default="BTCUSD", choices=["BTCUSD", "ETHUSD", "ETHBTC"],
                        help="The symbol to subscribe to")
    parser.add_argument("--levels", type=int, default=20, help="How many levels to desplay in the book")
    parser.add_argument("--real", action="store_true", help="Connect to real exchange")
    return parser

if __name__ == '__main__':

    parser = init_args()
    args = parser.parse_args()

    try:
        url = ""
        if args.real:
            print("\033[93m" + "Warning: Connecting to real exchange" + "\033[0m")
            url = "wss://api.gemini.com/v1"
        else:
            url = "wss://api.sandbox.gemini.com/v1"

        # TODO: Change to python.cmd for comfirmation

        print("Market Data: %s" % (url + "/marketdata/" + args.sym))
        print("Good? [Y/n]")
        line = sys.stdin.readline().strip()
        if not (line.lower() == "y" or line.lower() == "yes"):
            sys.exit(0)

        ui, book = init(args.levels)
        ws = websocket.WebSocketApp(url + "/marketdata/" + args.sym, on_message=parse)
        ws.run_forever(ping_interval=5)

    finally:

        terminate()
