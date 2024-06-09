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


def sort_dict_list(dict_list: List[Dict[str, Any]], order: str = 'desc') -> List[Dict[str, Any]]:
    """
Функция sort_dict_list сортирует список словарей по указанному порядку.

Args:
dict_list: список словарей, который требуется отсортировать
order: порядок сортировки ('asc' - по возрастанию, 'desc' - по убыванию). По умолчанию 'desc'.

"""
    return sorted(dict_list, key=lambda x: x['date'], reverse=(order == 'desc'))


#Ввод списка словарей
input_list: List[Dict[str, Any]] = eval(input())

#Ввод порядка сортировки
order_input: str = input("Введите 'asc' для сортировки по возрастанию или 'desc' для сортировки по убыванию: ")

sorted_list = sort_dict_list(input_list, order_input)
print(sorted_list)
