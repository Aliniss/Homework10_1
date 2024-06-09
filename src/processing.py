def filter_by_state(data, state='EXECUTED'):
    """Принимает список словарей и возвращает новый"""
    return [d for d in data if d.get('state') == state]


# Считываем список словарей со стандартного ввода
data = eval(input())

# Считываем значение для ключа state
state = input('Введите значение для ключа state (по умолчанию EXECUTED): ')

# Фильтруем список словарей
filtered_data = filter_by_state(data, state)

# Выводим результат
print(filtered_data)


def sort_dict_list(dict_list, order='desc'):
    """Принимает список словарей и возвращает отсортированный"""
    return sorted(dict_list, key=lambda x: x['date'], reverse=(order == 'desc'))


#Ввод списка словарей
input_list = eval(input())

#Ввод порядка сортировки
order_input = input("Введите 'asc' для сортировки по возрастанию или 'desc' для сортировки по убыванию: ")

sorted_list = sort_dict_list(input_list, order_input)
print(sorted_list)
