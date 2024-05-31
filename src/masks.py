def mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает маску."""

    # Проверяем, что длина номера карты больше или равна 10 (4 цифры видны, 6 цифр скрыты)
    if len(card_number) < 10:
        print("Недостаточно цифр. Добавьте 10 или более цифр в номер карты.")
        return card_number
    if "Visa Classic" in card_number:
        masked_number = card_number[:17] + card_number[18:20] + "** **** " + card_number[-4:]
        return masked_number
    elif "Visa Platinum" in card_number:
        masked_number = card_number[:18] + card_number[20:22] + "** **** " + card_number[-4:]
        return masked_number
    elif "Visa Gold" in card_number:
        masked_number = card_number[:14] +  card_number[15:17] + "** **** " + card_number[-4:]
        return masked_number
    elif "Maestro" in card_number:
        masked_number = card_number[:12] + card_number[13:15] + "** **** " + card_number[-4:]
        return masked_number
    elif "MasterCard" in card_number:
        masked_number = card_number[:16] + card_number[16:18] + "** **** " + card_number[-4:]
        return masked_number
    elif "Счет" in card_number:
        masked_account = card_number[:4] + " " + "**" + card_number[-4:]
        return masked_account


input_card_number = input("Введите номер карты: ")
masked_card_number = mask_card_number(input_card_number)
print(masked_card_number)