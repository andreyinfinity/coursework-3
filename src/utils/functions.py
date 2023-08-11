import json
from utils.transaction import Transaction


def load_file(filepath: str) -> list:
    """Открывает файл *.json"""
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def filter_dictionary_list(array: list, key, value) -> list:
    """Возвращает список словарей со значением 'value' в ключе 'key'."""
    def get_value(dictionary: dict,*args) -> bool:
        return dictionary.get(key) == value
    return list(filter(get_value, array))


def sorted_dictionary_list(array: list, key):
    """Сортирует список словарей по ключу 'key' по убыванию."""
    def get_value(dictionary: dict, *args) -> str:
        return dictionary.get(key)
    return array.sort(key=get_value, reverse=True)


def create_last_transactions(array: list, quantity: int):
    """Создает экземпляры класса Transaction с 'quantity' операциями"""
    transactions = []
    new_array = array[:quantity]
    for i in range(quantity):
        item = Transaction(new_array[i])
        transactions.append(item)
    return transactions
