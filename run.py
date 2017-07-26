import websocket
from parser import parse, terminate

try:

    ws = websocket.WebSocketApp("wss://api.gemini.com/v1/marketdata/BTCUSD", on_message=parse)
    ws.run_forever(ping_interval=5)

finally:

    terminate()
