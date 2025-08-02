import time
from src.bot import BinanceTraderBot
from binance.client import Client

STOCK_CODE = "SOL"
OPERATION_CODE = "SOLBRL"
CANDE_PERIOD = Client.KLINE_INTERVAL_15MINUTE
TRADED_QUANTITY = 10


def run_trader_sol():
    MATraderSOL = BinanceTraderBot(
        stock_code=STOCK_CODE,
        operation_code=OPERATION_CODE,
        traded_quantity=TRADED_QUANTITY,
        porcentage=100,
        candle_period=CANDE_PERIOD,
    )

    while 1:
        MATraderSOL.execute()
        time.sleep(60)
