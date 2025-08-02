from binance.client import Client
from binance.enums import *

from src.config import API_KEY, API_SECRET

client = Client(api_key=API_KEY, api_secret=API_SECRET)
