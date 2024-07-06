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


def read_csv(file_path):
    """Считывает данные из CSV файла и возвращает DataFrame."""
    return pd.read_csv(file_path)


def read_xlsx(file_path):
    """Считывает данные из XLSX файла и возвращает DataFrame."""
    return pd.read_excel(file_path, engine="openpyxl")
