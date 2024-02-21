from src.transaction_class import Transaction
from datetime import datetime
import pytest
from src import funcs


@pytest.fixture
def class_obj1():
    return Transaction(179194306, datetime(2019, 5, 19), "EXECUTED", "6381.58",
                       "USD", "USD", "Перевод организации",
                       "Visa Gold 8326537236216459", "Счет 58518872592028002662")


@pytest.fixture
def class_obj2():
    return Transaction(179194306, "2019-05-19T12:51:49.023880", "EXECUTED", "6381.58",
                       "USD", "USD", "Перевод организации",
                       "МИР 5211277418228469", None)


def test_load_data():
    assert type(funcs.load_data()) == list
