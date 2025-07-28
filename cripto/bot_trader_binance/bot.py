import os
import time
from datetime import datetime
import logging

import pandas as pd

from binance.client import Client
from binance.enums import *

from src.config import API_KEY, API_SECRET
from src.logger import createLogOrder


PAR = "DOGEBRL"
QUANTITY = 10.0
# Inicializa o cliente da Binance
# print(API_KEY)
client = Client(api_key=API_KEY, api_secret=API_SECRET)

status = client.get_account_status()
print(status)

# STOCK_CODE = "SOL"
# OPERATION_CODE = "SOLBRL"
STOCK_CODE = "BLR"
OPERATION_CODE = "BRLDOGE"
CANDE_PERIOD = Client.KLINE_INTERVAL_15MINUTE
TRADED_QUANTITY = 10

logging.basicConfig(
    filename="src/logs/trading_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class BinanceTraderBot:
    last_trader_decision: bool

    def __init__(
        self, stock_code, operation_code, traded_quantity, porcentage, candle_period
    ):
        self.stock_code = stock_code
        self.operation_code = operation_code
        self.traded_quantity = traded_quantity
        self.porcentage = porcentage
        self.candle_period = candle_period

        self.client = client

        self.update_all_data()

        print("-----------------------------------------")
        print("Bot iniciado")

    def update_all_data(self):
        self.account_data = self.get_updated_account_data()
        self.last_stock_acount_balance = self.get_last_stock_acount_balance()
        self.actual_trade_position = self.get_actual_trade_position()
        self.stock_data = self.get_stock_data_close_price_open_time()

    def get_updated_account_data(self):
        return self.client.get_account()

    def get_last_stock_acount_balance(self):
        for stock in self.account_data["balances"]:
            if stock["asset"] == self.stock_code:
                in_wallet_amount = stock["free"]
                break
        print(f"in_wallet_amount: ", float(in_wallet_amount))
        return float(in_wallet_amount)

    def get_actual_trade_position(self) -> bool:
        return self.last_stock_acount_balance > 0.001

    def get_stock_data_close_price_open_time(self):
        candles = self.client.get_klines(
            symbol=self.operation_code, interval=self.candle_period, limit=500
        )
        prices = pd.DataFrame(candles)

        prices.columns = [
            "open_time",
            "open_price",
            "high_price",
            "low_time",
            "close_price",
            "volume",
            "close_time",
            "quote_asset_volume",
            "number_of_trades",
            "taker_buy_base_asset_volume",
            "taker_buy_quote_asset_volume",
            "-",
        ]

        prices = prices[["close_price", "open_time"]]

        prices["open_time"] = pd.to_datetime(
            prices["open_time"], unit="ms"
        ).dt.tz_localize("UTC")

        prices["open_time"] = prices["open_time"].dt.tz_convert("America/Sao_Paulo")

        return prices

    def get_moving_average_trade_strategy(self, fast_window=7, slow_window=40):
        self.stock_data["ma_fast"] = (
            self.stock_data["close_price"].rolling(window=fast_window).mean()
        )
        self.stock_data["ma_slow"] = (
            self.stock_data["close_price"].rolling(window=slow_window).mean()
        )

        last_ma_fast = self.stock_data["ma_fast"].iloc[-1]
        last_ma_slow = self.stock_data["ma_slow"].iloc[-1]

        if last_ma_fast > last_ma_slow:
            ma_trade_decision = True
        else:
            ma_trade_decision = False

        print("--------------------------------------")
        print("Estrategia executada: Moving Average")
        print(
            f"({self.operation_code})\n | {last_ma_fast:.3f} = Útima Média Rápidda \n {last_ma_slow:.3f} = Útima Média Lenta"
        )

        print(f"Decisão: {"Comprar" if ma_trade_decision == True else "Vender"}")
        print("--------------------------------------")

        return ma_trade_decision

    def buy_stock(self):
        if self.actual_trade_position == False:
            print("Realizando Compra")
            order_buy = self.client.create_order(
                symbol=self.operation_code,
                side=SIDE_BUY,
                type=ORDER_TYPE_MARKET,
                quantity=self.traded_quantity,
            )
            self.actual_trade_position = True
            createLogOrder(order_buy)
            print("Finalizado Compra: ", order_buy)
            return order_buy
        else:
            logging.warning("Error ao comprar")
            print("Error ao comprar")
            return False

    def sell_stock(self):
        if self.actual_trade_position == True:
            print("Realizando Venda")
            quantity = int(self.last_stock_acount_balance * 1000) / 1000
            print(self.last_stock_acount_balance)
            print(quantity)
            # print("step_size")
            # exchange = self.get_exchange()
            # value = int(self.last_stock_acount_balance * exchange["step_size"])
            # print(value)
            # step_size = value / exchange["step_size"]

            # print(step_size)
            if quantity < 10:
                logging.warning(
                    f"A quantidade dispovel é menor que 10: total disponivel {quantity}"
                )
                return False
            order_sell = self.client.create_order(
                symbol=self.operation_code,
                side=SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity,
            )
            self.actual_trade_position = False
            createLogOrder(order_sell)
            print("Finalizado Venda: ", order_sell)
            return order_sell
        else:
            logging.warning("Error ao Vender")
            print("Error ao Vender")
            return False

    def print_wallet(self):
        for stock in self.account_data["balances"]:
            if float(stock["free"]) > 0:
                print(stock)
                break

    def print_stock(self):
        for stock in self.account_data["balances"]:
            if stock["asset"] == self.stock_code:
                print(stock)
                break

    def print_brl(self):
        for stock in self.account_data["balances"]:
            if stock["asset"] == "BRL":
                print(stock)
                break

    def get_wallet(self):
        for stock in self.account_data["balances"]:
            if float(stock["free"]) > 0:
                print(stock)
                return stock

    def get_stock(self):
        for stock in self.account_data["balances"]:
            if stock["asset"] == self.stock_code:
                print(stock)
                return stock

    def execute(self):
        self.update_all_data()
        print("-----------------------------")
        print(f"Executando ({datetime.now().strftime("%Y-%m-%d %H:%M:%S")})")
        print(
            f"Posição atual: {"Comprado" if MATrader.actual_trade_position else "Vendido"}"
        )
        print(
            f"Balanço atual: {MATrader.last_stock_acount_balance} | ({self.stock_code})"
        )
        ma_trade_description = self.get_moving_average_trade_strategy()

        self.last_trader_decision = ma_trade_description

        if self.actual_trade_position == False and self.last_trader_decision == True:
            self.print_stock()
            self.print_brl()
            self.buy_stock()
            time.sleep(2)
            self.update_all_data()
            self.print_stock()
            self.print_brl()

        elif self.actual_trade_position == True and self.last_trader_decision == False:
            self.print_stock()
            self.print_brl()
            self.sell_stock()
            time.sleep(2)
            self.update_all_data()
            self.print_stock()
            self.print_brl()

        print("-----------------------------")

    def get_exchange(self):
        info = client.get_exchange_info()
        data = {}
        for s in info["symbols"]:
            if s["symbol"] == PAR:
                for f in s["filters"]:

                    if f["filterType"] == "LOT_SIZE":
                        min_qty = float(f["minQty"])
                        max_qty = float(f["maxQty"])
                        step_size = float(f["stepSize"])
                        data = {
                            "min_qty": min_qty,
                            "max_qty": max_qty,
                            "step_size": step_size,
                        }
                        break
                break
        return data


MATrader = BinanceTraderBot(
    stock_code=STOCK_CODE,
    operation_code=OPERATION_CODE,
    traded_quantity=TRADED_QUANTITY,
    porcentage=100,
    candle_period=CANDE_PERIOD,
)


while 1:
    MATrader.execute()
    time.sleep(60)
