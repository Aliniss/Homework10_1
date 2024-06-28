from typing import List, Dict, Any


def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
Функция фильтрует данные по указанному состоянию

Args:
data (List[Dict[str, Any]]): список словарей с данными
state (str): состояние, по которому необходимо отфильтровать данные (по умолчанию 'EXECUTED')
    """
    return [d for d in data if d.get('state') == state]


def sort_by_date(date_list: list, reverse_list: bool = True) -> list | bool:
    """Return filtered list by date"""
    sorted_list = sorted(date_list, key=lambda date_dict: date_dict.get("date"), reverse=reverse_list)
    return sorted_list
