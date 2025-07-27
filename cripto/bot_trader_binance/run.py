from binance.client import Client
from binance.enums import *

import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
PAR = "DOGEBRL"

# Inicializa o cliente da Binance
# print(API_KEY)
client = Client(api_key=API_KEY, api_secret=API_SECRET)

status = client.get_account_status()
print(status)


def get_my_criptos():
    info = client.get_account()
    # print(info["balances"])

    for crip in info["balances"]:
        if float(crip["free"]) > 0:
            print(crip)


def comprar():
    ordem = client.create_order(
        symbol=PAR, quantity=1.0, side=SIDE_SELL, type=ORDER_TYPE_MARKET
    )
    print("✅ Ordem de compra executada: ", ordem)


get_my_criptos()
print()
comprar()
get_my_criptos()

# get_my_criptos()


def obter_ticker():
    ticker = client.get_symbol_ticker(symbol=PAR)
    data = float(ticker["price"])
    print(data)
    return data


# obter_ticker()
