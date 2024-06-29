from src.generators import transactions, filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency():
    assert next(filter_by_currency(transactions, "RUB")) == 873106923


def test_transaction_descriptions():
    assert next(transaction_descriptions(transactions)) == "Перевод организации"


def test_card_number_generator():
    assert next(card_number_generator(1, 1)) == "0000 0000 0000 0001"
