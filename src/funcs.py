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
