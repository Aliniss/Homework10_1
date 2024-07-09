import json
from json import JSONDecodeError
import logging
import pandas as pd

import re
from collections import Counter

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log", mode='w')
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_json_transactions(file_path: str) -> list[dict] or []:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях."""
    try:

        with open(file_path, "r", encoding="utf-8") as file:
            transaction = json.loads(file.read())

            logger.info(f"Получаем данные о финансовых транзакциях {transaction}")

            return transaction
    except JSONDecodeError:
        logger.error("Ошибка декодирования JSON")
        return []


if __name__ == "__main__":
    file_path = r"C:\Users\Azerty\PycharmProjects\Homework\data\operations.json"
    transactions = get_json_transactions(file_path)
    print(transactions)


def get_xlsx_file(filepath: str) -> dict:
    """
    Реализовывает считывание финансовых операций с XLSX-файлов
    """
    reviews = pd.read_excel(filepath)
    filepath_dict = reviews.to_dict()
    return filepath_dict


def get_csv_file(filepath: str) -> dict:
    """
    Реализовывает считывание финансовых операций с CSV-файлов
    """
    reviews = pd.read_csv(filepath, sep=";")
    filepath_dict = reviews.to_dict()
    return filepath_dict


def find_string(transactions: list, search_bar: str) -> list:
    result = []
    pattern = re.compile(search_bar, re.IGNORECASE)
    for transaction in transactions:
        if pattern.search(transaction["description"]):
            result.append(transaction)
    return result


def get_dict(transactions: list, categories: dict) -> dict:
    pattern_1 = re.compile("Перевод организации", re.IGNORECASE)
    pattern_2 = re.compile("Перевод со счета на счет", re.IGNORECASE)
    pattern_3 = re.compile("Перевод с карты на карту", re.IGNORECASE)

    counter = Counter(transaction["description"] for transaction in transactions)

    categories["Перевод организации"] += counter[pattern_1.pattern]
    categories["Перевод со счета на счет"] += counter[pattern_2.pattern]
    categories["Перевод с карты на карту"] += counter[pattern_3.pattern]

    return categories


print(
    get_dict(
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160",
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657",
            },
        ], {"Перевод организации": 0, "Перевод со счета на счет": 0, "Перевод с карты на карту": 0}
    )
)
