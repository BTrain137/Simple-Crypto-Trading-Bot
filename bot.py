import websocket, json, pprint, talib, numpy

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

def on_open(ws):
  print("open connection")

def on_close(ws):
  print("closed connection")

def on_message(ws, message):
  print("received message")
  json_message  = json.loads(message)
  # pprint.pprint(json_message)

  candle = json_message['k']

  is_candle_closed = candle['x']
  close_price = candle['c']
  open_price = candle['o'];

  print(is_candle_closed)
  print(close_price)
  print(open_price)

  if is_candle_closed:
    print("!!!!!!!!!!candle closed at {}!!!!!!!!!!!!".format(close_price))

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()

