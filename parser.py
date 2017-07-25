import json

def parse(ws, message):
    parsed = json.loads(message)
    print("type: %s, seq #: %s" % (parsed["type"], parsed["eventId"]), end="")
