from utils.functions import load_file, filter_dictionary_list, sorted_dictionary_list, create_last_transactions

# Путь к файлу со всеми транзакциями и количество последних транзакций для вывода
OPERATIONS = "data/operations.json"
last_transactions = 5

all_operations = load_file(OPERATIONS)

executed_operations = filter_dictionary_list(all_operations, 'state', 'EXECUTED')

sorted_dictionary_list(executed_operations, 'date')

transactions = create_last_transactions(executed_operations, last_transactions)

for transaction in transactions:
    print(transaction.get_transaction_form())
