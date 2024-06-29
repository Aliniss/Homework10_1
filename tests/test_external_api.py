import unittest
from unittest.mock import patch

from src.external_api import get_amount_rub, get_transactions


class TestCurrencyConversion(unittest.TestCase):

    @patch("src.external_api.requests.get")
    def test_get_amount_rub_with_rub(self, mock_get):
        # Тест для случая, когда валюта уже в рублях
        transaction = {"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}}
        result = get_amount_rub(transaction)
        self.assertEqual(result, 1000.0)
        mock_get.assert_not_called()

    @patch("src.external_api.requests.get")
    def test_get_amount_rub_with_usd(self, mock_get):
        # Тест для случая, когда валюта в долларах
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"result": 75000}
        transaction = {"operationAmount": {"amount": "1000", "currency": {"code": "USD"}}}
        result = get_amount_rub(transaction)
        self.assertEqual(result, 75000.0)
        mock_get.assert_called_once()

    @patch("src.external_api.requests.get")
    def test_get_amount_rub_with_unsupported_currency(self, mock_get):
        # Тест для случая с неподдерживаемой валютой
        transaction = {"operationAmount": {"amount": "1000", "currency": {"code": "GBP"}}}
        result = get_amount_rub(transaction)
        self.assertEqual(result, 0.0)
        mock_get.assert_not_called()

    @patch("src.external_api.requests.get")
    def test_get_transactions(self, mock_get):
        # Тест для проверки списка транзакций
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.side_effect = [
            {"result": 75000},  # Ответ для USD
            {"result": 88000},  # Ответ для EUR
        ]
        transactions = [
            {"operationAmount": {"amount": "1000", "currency": {"code": "USD"}}},
            {"operationAmount": {"amount": "1000", "currency": {"code": "EUR"}}},
            {"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}},
        ]
        result = get_transactions(transactions)
        self.assertEqual(result, [75000.0, 88000.0, 1000.0])
        self.assertEqual(mock_get.call_count, 2)
