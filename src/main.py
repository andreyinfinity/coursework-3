from utils.functions import load_file, filter_executed, sorted_by_date, create_list_transactions

# Путь к файлу со всеми транзакциями и количество последних транзакций для вывода
OPERATIONS = "data/operations.json"
total_transactions = 5

all_operations = load_file(OPERATIONS)

executed_operations = filter_executed(all_operations)

sorted_by_date(executed_operations)

transactions = create_list_transactions(executed_operations, total_transactions)

for transaction in transactions:
    print(transaction.get_transaction_form())
