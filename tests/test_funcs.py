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


@pytest.fixture
def class_obj3():
    return Transaction(441945886, "2019-08-26T10:50:58.294041", "EXECUTED", "31957.58",
                       "руб.", "RUB", "Перевод организации",
                       "Maestro 1596837868705199", "Счет 64686473678894779589")


def test_load_data():
    assert type(funcs.load_data()) == list


def test_get_transactions_list(class_obj3):
    transactions = funcs.load_data()
    assert funcs.get_transactions_list(transactions) == [class_obj3]
    

def test_remove_disabled_transactions(class_obj1, class_obj2, class_obj3):
    assert funcs.remove_disabled_transactions([class_obj1, class_obj2, class_obj3]) == [class_obj1, class_obj3]


def test_modificate_time_format(class_obj2):
    funcs.modificate_time_format([class_obj2])
    assert class_obj2.date == datetime(2019, 5, 19, 12, 51, 49, 23880)
