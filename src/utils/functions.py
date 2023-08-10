import json


def load_file(filepath) -> list:
    """Открывает файл *.json"""
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_file(filepath, array):
    """Сохраняет файл *.json"""
    # добавил параметры, чтобы кириллица и отступы в файле отображались корректно
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(array, file, ensure_ascii=False, indent=4)


def filter_executed(array):
    """Возвращает список выполненных транзакций"""
    # фильтр реализован через перебор по списку словарей с получением ключа по методу get,
    # чтобы избежать ошибки, если в словарь окажется пустой или с отсутствующим ключом
    new_array = []
    for item in array:
        if item.get('state') == 'EXECUTED':
            new_array.append(item)
    return new_array


def sorted_by_date(array):
    """Сортирует список по ключу 'date'"""
    pass


def create_list_transactions(array):
    """Создает экземпляры класса Transaction с 5 последними операциями"""
    pass
