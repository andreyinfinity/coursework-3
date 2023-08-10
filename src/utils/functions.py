import json
from utils.transaction import Transaction


def load_file(filepath) -> list:
    """Открывает файл *.json"""
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def filter_executed(array):
    """Возвращает список выполненных транзакций"""
    # фильтр реализован через перебор по списку словарей с получением ключа по методу get,
    # чтобы избежать ошибки, если в словарь окажется пустой или с отсутствующим ключом
    new_array = []
    for item in array:
        if item.get('state') == 'EXECUTED':
            new_array.append(item)
    return new_array


def get_value(dictionary: dict) -> str:
    return dictionary.get('date')


def sorted_by_date(array):
    """Сортирует список по ключу 'date' по убыванию даты"""
    return array.sort(key=get_value, reverse=True)


def create_list_transactions(array: list, total: int):
    """Создает экземпляры класса Transaction с 5 последними операциями"""
    transactions = []
    new_array = array[:total]
    for i in range(total):
        item = Transaction(new_array[i])
        transactions.append(item)
    return transactions
