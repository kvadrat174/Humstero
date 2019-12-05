#!/usr/bin/env python
import requests
import json


bitcoin_api_url = 'https://blockchain.info/ticker'

def get_latest_bitcoin_price():
    response = requests.get(bitcoin_api_url)
    response_json = response.json()
    # Конвертирует курс в число с плавающей запятой
    return float(response_json['USD']['last'])

