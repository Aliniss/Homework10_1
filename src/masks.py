def mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает маску."""

    # Проверяем, что длина номера карты больше или равна 10 (4 цифры видны, 6 цифр скрыты)
    if len(card_number) < 10:
        print("Недостаточно цифр. Добавьте 10 или более цифр в номер карты.")
        return card_number

    # Удаляем пробелы из номера карты
    card_number = card_number.replace(" ", "")

    # Заменяем цифры в середине на "**"
    masked_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]

    return masked_number


input_card_number = input("Введите номер карты: ")
masked_card_number = mask_card_number(input_card_number)
print(masked_card_number)


def mask_account_number(account_number: str) -> str:
    """Принимает на вход номер счёта и возвращает маску."""

    # Проверяем, что длина номера счета больше или равна 4 (все остальные цифры скрыты)
    if len(account_number) < 4:
        print("Недостаточно цифр. Добавьте 4 или более цифры в номер счета.")
        return account_number

    # Удаляем пробелы из номера счета
    account_number = account_number.replace(" ", "")

    # Оставляем только последние 4 цифры
    masked_number = "**" + account_number[-4:]

    return masked_number


input_account_number = input("Введите номер счета: ")
masked_account_number = mask_account_number(input_account_number)
print(masked_account_number)
