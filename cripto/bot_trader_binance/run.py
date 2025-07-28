from binance.client import Client
from binance.enums import *

import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
# PAR = "DOGEBRL"
PAR = "DOGEBRL"
QUANTITY = 5.0
# Inicializa o cliente da Binance
# print(API_KEY)
client = Client(api_key=API_KEY, api_secret=API_SECRET)

status = client.get_account_status()
print(status)


def get_exchange():
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
    # Now, use min_qty, max_qty, and step_size to validate and adjust your order quantity
    # For example, to ensure correct precision:
    # adjusted_quantity = round(desired_quantity / step_size) * step_size


def get_my_criptos():
    info = client.get_account()
    # print(info["balances"])

    for crip in info["balances"]:
        if float(crip["free"]) > 0:
            print(crip)


def get_symbol_info():
    test = client.get_symbol_info(PAR)
    # print(test["filters"])
    for v in test["filters"]:
        print(v)


def get_min_notional():
    test = client.get_symbol_info(PAR)
    print(test["filters"][6])
    print()
    # print(test["filters"])


def comprar():
    ordem = client.order_market_buy(symbol=PAR, quantity=QUANTITY)
    print("✅ Ordem de compra executada:", ordem)


def exchange_info():
    info = client.get_exchange_info()
    print(info)


get_my_criptos()
print()
exchange = get_exchange()
print(exchange)
step_size = int(float(23.98600000) * exchange["step_size"]) / exchange["step_size"]

print()
print(step_size)


# comprar()
# get_my_criptos()


get_min_notional()
# exchange_info()
# get_my_criptos()


def obter_ticker():
    ticker = client.get_symbol_ticker(symbol=PAR)
    data = float(ticker["price"])
    print(data)
    return data


# obter_ticker()
