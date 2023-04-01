from oanda_api import OandaAPI

api = OandaAPI()

while True:
    command = input("Enter command:")
    if command == "T":
        print("Make a trade")
        trade_id, ok = api.place_trade("EUR_USD", 10, take_profit=1.15123400, stop_loss=1.09000100)
        print('trade_id', trade_id, ok)
    if command == "C":
        print('Closing', trade_id)
        print(api.close_trade(trade_id))
    if command == "Q":
        break