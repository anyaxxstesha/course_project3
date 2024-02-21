from src import funcs

data = funcs.load_data()
transactions = funcs.get_transactions_list(data)
correct_transactions = funcs.remove_disabled_transactions(transactions)
datetime_transactions = funcs.modificate_time_format(correct_transactions)
sorted_transactions = funcs.sort_transactions_by_date(datetime_transactions)
funcs.show_latest_transactions(sorted_transactions)
