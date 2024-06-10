from typing import List, Dict, Any


def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
Функция фильтрует данные по указанному состоянию

Args:
data (List[Dict[str, Any]]): список словарей с данными
state (str): состояние, по которому необходимо отфильтровать данные (по умолчанию 'EXECUTED')
    """
    return [d for d in data if d.get('state') == state]


# Считываем список словарей со стандартного ввода
data = eval(input())

# Считываем значение для ключа state
state = input('Введите значение для ключа state (по умолчанию EXECUTED): ')

# Фильтруем список словарей
filtered_data = filter_by_state(data, state)

# Выводим результат
print(filtered_data)


def sort_by_date(dict_list: List, order: bool = True) -> List | bool:
    """
Функция sort_dict_list сортирует список словарей по указанному порядку.

Args:
dict_list: список словарей, который требуется отсортировать
order: порядок сортировки ('True' - по возрастанию, 'False' - по убыванию). По умолчанию 'True'.

"""
    return sorted(dict_list, key=lambda x: x['date'], reverse=order)


#Ввод списка словарей
input_list: List[Dict[str, Any]] = eval(input())

#Ввод порядка сортировки
order_input: bool = bool(input("Введите 'True' для сортировки по возрастанию или 'False' для сортировки по убыванию: "))

sorted_list = sort_by_date(input_list, order_input)
print(sorted_list)
