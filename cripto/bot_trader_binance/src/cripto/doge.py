import time
from src.bot import BinanceTraderBot
from binance.client import Client

STOCK_CODE = "DOGE"
OPERATION_CODE = "DOGEBRL"
CANDE_PERIOD = Client.KLINE_INTERVAL_15MINUTE
TRADED_QUANTITY = 10


def run_trader_doge():
    MATraderDOGE = BinanceTraderBot(
        stock_code=STOCK_CODE,
        operation_code=OPERATION_CODE,
        traded_quantity=TRADED_QUANTITY,
        porcentage=100,
        candle_period=CANDE_PERIOD,
    )

    while 1:
        MATraderDOGE.execute()
        time.sleep(60)
