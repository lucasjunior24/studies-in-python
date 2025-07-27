from binance.client import Client
from binance.enums import *
import time

# from app.config import API_KEY, API_SECRET

# Inicializa o cliente da Binance
client = Client(API_KEY, API_SECRET)

# Configurações do bot
TRADING_PAIR = 'BTCUSDT'
QUANTIDADE = 0.001
LIMITE_COMPRA = 58000  # exemplo: compra se cair abaixo disso

def checar_preco():
    ticker = client.get_symbol_ticker(symbol=TRADING_PAIR)
    return float(ticker['price'])

def comprar():
    ordem = client.order_market_buy(
        symbol=TRADING_PAIR,
        quantity=QUANTIDADE
    )
    print("✅ Ordem de compra executada:", ordem)

def bot_loop():
    while True:
        try:
            preco = checar_preco()
            print(f"Preço atual de {TRADING_PAIR}: ${preco}")

            if preco < LIMITE_COMPRA:
                print(f"🔽 Preço abaixo de {LIMITE_COMPRA}. Tentando comprar...")
                comprar()
                break  # Encerra após comprar, ou remova se quiser continuar

            time.sleep(10)  # Espera 10 segundos antes de checar novamente
        except Exception as e:
            print("Erro:", e)
            time.sleep(5)

if __name__ == '__main__':
    bot_loop()
