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
