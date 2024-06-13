import pytest
from typing import List, Dict, Any
from src.processing import filter_by_state


@pytest.fixture
def list_for_test():
    list_for_function = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    return [list_for_function, 'EXECUTED']


def test_filter_by_state(list_for_test: List[Dict[str, Any]]):
    assert filter_by_state(list_for_test)
