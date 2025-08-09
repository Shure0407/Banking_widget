from typing import Any

import pytest

from src import generators


@pytest.fixture
def data_tr() -> Any:
    return (
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 945619570,
            "state": "EXECUTED",
            "date": "2018-08-20T03:09:58.425572",
            "operationAmount": {"amount": "11111.07", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "Счет 6830613657916888",
            "to": "Счет 6614605963066777",
        },
        {
            "id": 945619789,
            "state": "EXECUTED",
            "date": "2018-09-10T04:10:58.425572",
            "operationAmount": {"amount": "2222.07", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916999",
            "to": "Счет 11776614605963066555",
        },
    )


def test_filter_by_currency(data_tr: Any) -> Any:
    """Тестирование с использованием фикстуры функции приема на вход список словарей, представляющих транзакции и
    возвращает итератор транзакций, где валюта операций соответствует заданной"""

    assert list(generators.filter_by_currency(data_tr, "USD")) == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
    assert list(generators.filter_by_currency(data_tr, "RUB")) == [
        {
            "id": 945619570,
            "state": "EXECUTED",
            "date": "2018-08-20T03:09:58.425572",
            "operationAmount": {"amount": "11111.07", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "Счет 6830613657916888",
            "to": "Счет 6614605963066777",
        },
        {
            "id": 945619789,
            "state": "EXECUTED",
            "date": "2018-09-10T04:10:58.425572",
            "operationAmount": {"amount": "2222.07", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916999",
            "to": "Счет 11776614605963066555",
        },
    ]
    assert list(generators.filter_by_currency(data_tr, " ")) == []
    assert list(generators.filter_by_currency(data_tr, "_")) == []


def test_transaction_descriptions(data_tr: list) -> Any:
    """Тестирование с использованием фикстуры функции приема на вход список словарей, представляющих транзакции и
    возвращает описание каждой операции по очереди"""
    assert list(generators.transaction_descriptions(data_tr)) == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    description = generators.transaction_descriptions(data_tr)
    assert next(description) == "Перевод организации"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод с карты на карту"
    assert next(description) == "Перевод организации"


def test_card_number_generator() -> Any:
    """Тестирование функции генератор, который выдает номера банковских карт"""

    generator = generators.card_number_generator()
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
