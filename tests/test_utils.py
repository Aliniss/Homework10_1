import unittest
from json.decoder import JSONDecodeError
from unittest.mock import mock_open, patch
import pandas as pd

from src.utils import get_json_transactions, read_csv, read_xlsx


class TestGetJsonTransactions(unittest.TestCase):
    @patch("src.utils.json.loads")
    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": "100.00"}]')
    def test_get_json_transactions_valid(self, mock_open, mock_json_loads):
        # Устанавливаем возвращаемое значение mock_json_loads
        mock_json_loads.return_value = [{"id": 1, "amount": "100.00"}]
        result = get_json_transactions("dummy_path.json")
        self.assertEqual(result, [{"id": 1, "amount": "100.00"}])
        mock_open.assert_called_once_with("dummy_path.json", "r", encoding="utf-8")
        mock_json_loads.assert_called_once()

    @patch("src.utils.json.loads", side_effect=JSONDecodeError("Expecting value", "", 0))
    @patch("builtins.open", new_callable=mock_open, read_data="Некорректный JSON")
    def test_get_json_transactions_invalid(self, mock_open, mock_json_loads):
        result = get_json_transactions("dummy_path.json")
        self.assertEqual(result, [])
        mock_open.assert_called_once_with("dummy_path.json", "r", encoding="utf-8")
        mock_json_loads.assert_called_once()


@patch("pandas.read_csv")
def test_read_csv(mock_read_csv):
    mock_read_csv.return_value = pd.DataFrame({"data": [1, 2, 3]})
    df = read_csv("dummy.csv")
    assert not df.empty


@patch("pandas.read_excel")
def test_read_xlsx(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame({"data": [1, 2, 3]})
    df = read_xlsx("dummy.xlsx")
    assert not df.empty
