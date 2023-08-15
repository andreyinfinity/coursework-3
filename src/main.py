from utils.functions import load_file, filter_dictionary_list, sorted_dictionary_list
from utils.transactions import Transactions

# Путь к файлу со всеми транзакциями и количество последних транзакций для вывода
OPERATIONS = "data/operations.json"
last_transactions = 5

# Загрузка файла с транзакциями
all_operations = load_file(OPERATIONS)

executed_operations = filter_dictionary_list(all_operations, 'state', 'EXECUTED')

sorted_dictionary_list(executed_operations, 'date')

new_array = executed_operations[:last_transactions]
transactions = Transactions(new_array)

print(*transactions.take_statistic(), sep='\n')
