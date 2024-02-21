import json
import datetime
from .transaction_class import Transaction


def load_data() -> list:
    """
    Загружает список транзакций из файла
    """
    with open('./operations.json', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_transactions_list(data: list) -> list:
    """
    Инициализирует экземпляр класса и составляет список из экземпляров класса
    """

    transactions = []
    for i in range(len(data)):
        id_ = data[i].get("id")
        date = data[i].get("date")
        state = data[i].get("state")
        operation_amount = data[i].get("operationAmount", {}).get("amount")
        currency_name = data[i].get("operationAmount", {}).get("currency", {}).get("name")
        currency_code = data[i].get("operationAmount", {}).get("currency", {}).get("code")
        description = data[i].get("description")
        from_ = data[i].get("from")
        to = data[i].get("to")
        transaction = Transaction(id_, date, state, operation_amount, currency_name,
                                  currency_code, description, from_, to)
        transactions.append(transaction)
    return transactions


def remove_disabled_transactions(transactions: list) -> list:
    """
    Удаляет не исполненные транкзаии и сломанные транкзации
    """
    correct_transactions = list(filter(lambda i: not i.is_broken and i.state == "EXECUTED", transactions))
    return correct_transactions


def modificate_time_format(correct_transactions: list) -> list:
    """
    Из формата ISO 8601 преобразовать дату и время транкзации в объект datetime
    """
    for i in range(len(correct_transactions)):
        dt_str = correct_transactions[i].date
        dt = datetime.datetime.fromisoformat(dt_str)
        correct_transactions[i].date = dt
    return correct_transactions


def sort_transactions_by_date(correct_transactions: list) -> list:
    """
    Сортирует транкзации по дате
    """
    correct_transactions.sort(key=lambda transaction: transaction.date)
    return correct_transactions


def show_latest_transactions(correct_transactions: list):
    """
    Выводит 5 последних транкзаций
    """
    amount_to_show = 5
    for i in range(amount_to_show):
        correct_transactions[i].encode_important_data()
        print(correct_transactions[i].show())
