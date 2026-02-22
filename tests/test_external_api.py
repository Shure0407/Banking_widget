from unittest.mock import patch

from src import external_api

import pytest


data_u = {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702",
}


@patch("requests.get")
def test1_conversion(mock_get):
    """Тестирование функции conversion с помощью декоратора patch"""

    mock_get.return_value.json.return_value = {"result": "31957.58"}
    assert external_api.conversion(data_u) == 31957.58


@pytest.fixture
def data_r():
    """Фикстура части преобразованного файла из json в python"""

    return (
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "CHN", "code": "CHN"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
    )


def test2_conversion(data_r: dict) -> float | None:
    """Тестирование функции conversion, не связанные с API"""

    assert external_api.conversion(data_r[0]) == 9824.07
    assert external_api.conversion(data_r[1]) == []
