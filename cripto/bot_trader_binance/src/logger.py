import logging
from datetime import datetime


logging.basicConfig(
    filename="src/logs/trading_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def createLogOrder(order):
    side = order["side"]
    type = order["type"]
    quantity = order["executedQty"]
    asset = order["symbol"]
    price_per_unit = order["fills"][0]["price"]
    currency = order["fills"][0]["commissionAsset"]
    total_value = order["cummulativeQuoteQty"]
    timestamp = order["transactTime"]

    datetime_transact = datetime.utcfromtimestamp(timestamp / 1000).strftime(
        "(%H:%M:%S) %Y-%m-%d"
    )
    log_message = (
        "-----------------------------------\n"
        "ORDEN EXECUTADA: \n"
        f"Side: {side}\n"
        f"Ativo: {asset}\n"
        f"Quantidadde: {quantity}\n"
        f"VALOR NO MOMENTO: {price_per_unit}\n"
        f"Moeda: {currency}\n"
        f"Valor em: {currency}: {total_value}\n"
        f"Type: {type}\n"
        f"Data/Hora: {datetime_transact}\n"
        "\n"
        "COMPLETE ORDER: \n"
        f"{order}"
        "\n-----------------------------------\n"
    )

    print_message = (
        "-----------------------------------\n"
        "ORDEN EXECUTADA: \n"
        f"Side: {side}\n"
        f"Ativo: {asset}\n"
        f"Quantidadde: {quantity}\n"
        f"VALOR NO MOMENTO: {price_per_unit}\n"
        f"Moeda: {currency}\n"
        f"Valor em: {currency}: {total_value}\n"
        f"Type: {type}\n"
        f"Data/Hora: {datetime_transact}\n"
        "\n-----------------------------------\n"
    )

    print(print_message)

    logging.info(log_message)
