import json
from json import JSONDecodeError
import logging
import pandas as pd

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
