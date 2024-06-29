import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
url = "https://api.apilayer.com/exchangerates_data/convert?to={}&from={}&amount={}"
headers = {"apikey": API_KEY}


def get_amount_rub(transactions: dict) -> float:
    """Функция переводит транзакции в рубли"""

    amount = transactions.get("operationAmount", {}).get("amount")
    currency = transactions.get("operationAmount", {}).get("currency", {}).get("code")

    if currency == "RUB":
        return float(amount)
    elif currency in ["USD", "EUR"]:
        response = requests.get(url.format("RUB", currency, amount), headers=headers)
        if response.status_code == 200:
            data = response.json()
            return float(data["result"])
        else:
            return 0.0
    else:
        return 0.0


def get_transactions(transactions: list[dict]) -> list[float]:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    list_transactions = []
    for transaction in transactions:
        amount_rub = get_amount_rub(transaction)
        list_transactions.append(amount_rub)
    return list_transactions
