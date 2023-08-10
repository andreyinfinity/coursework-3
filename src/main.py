from utils.functions import load_file, filter_executed, save_file

OPERATIONS = "data/operations.json"
EXECUTED_OPERATIONS = "data/ex_operations.json"

all_operations = load_file(OPERATIONS)

executed_operations = filter_executed(all_operations)

save_file(EXECUTED_OPERATIONS, executed_operations)
