import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/ masks.log")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def mask_card_number(card_number: str) -> str | None:
    """
Функция принимает на вход номер кредитной карты в виде строки и возвращает строку с маскированным номером.

Args:
card_number: str - номер кредитной карты
"""

    #   Проверяем тип карты
    if "Visa Classic" in card_number:
        masked_number = card_number[:17] + " " + card_number[18:20] + "** **** " + card_number[-4:]
        logger.info(f"Получаем зашифрованный номер карты {masked_number}")
        return masked_number
    elif "Visa Platinum" in card_number:
        masked_number = card_number[:18] + " " + card_number[19:21] + "** **** " + card_number[-4:]
        logger.info(f"Получаем зашифрованный номер карты {masked_number}")
        return masked_number
    elif "Visa Gold" in card_number:
        masked_number = card_number[:14] + " " + card_number[15:17] + "** **** " + card_number[-4:]
        logger.info(f"Получаем зашифрованный номер карты {masked_number}")
        return masked_number
    elif "Maestro" in card_number:
        masked_number = card_number[:12] + " " + card_number[13:15] + "** **** " + card_number[-4:]
        logger.info(f"Получаем зашифрованный номер карты {masked_number}")
        return masked_number
    elif "MasterCard" in card_number:
        masked_number = card_number[:16] + " " + card_number[16:18] + "** **** " + card_number[-4:]
        logger.info(f"Получаем зашифрованный номер карты {masked_number}")
        return masked_number
    elif "Maestro" in card_number:
        masked_number = card_number[:12] + " " + card_number[13:15] + "** **** " + card_number[-4:]
        logger.info(f"Получаем зашифрованный номер карты {masked_number}")
        return masked_number
    elif "Счет" in card_number:
        masked_account = card_number[:4] + " " + "**" + card_number[-4:]

        logger.info(f"Получаем зашифрованный номер карты {masked_account}")

        return masked_account
    return None


def convert_date(date_str: str) -> str:
    """
    Принимает на вход строку и преобразует её в дату

    Args:
    date_str (str): строка с датой
    """
    date_parts = date_str.split("T")[0].split("-")
    year = date_parts[0]
    month = date_parts[1]
    day = date_parts[2]
    return f"{day}.{month}.{year}"
