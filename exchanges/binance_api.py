from binance.client import Client
from config import BINANCE_API_KEY, BINANCE_API_SECRET

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

def get_binance_markets():
    return [s["symbol"] for s in client.get_exchange_info()["symbols"]]
