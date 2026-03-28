from unittest.mock import patch

from unittest.mock import Mock

from src.tables import tables_csv

from src.tables import tables_excel


@patch("csv.DictReader")
def test_tables_csv(mock_read_csv):
    """Тестирование функции tables с помощью декоратора patch"""

    mock_read_csv.return_value = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "593027",
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": "30368",
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
    ]
    assert tables_csv("C:/Users/Aleksandr/PycharmProjects/PythonProject/data/transactions_three_str.csv") == [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": "593027",
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": "30368",
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
    ]


def test_tables_excel():
    """Тестирование функции tables_excel с помощью декоратора patch"""

    mock_read_excel = Mock(
        return_value=[
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            },
            {
                "id": 3598919,
                "state": "EXECUTED",
                "date": "2020-12-06T23:00:58Z",
                "amount": 29740,
                "currency_name": "Peso",
                "currency_code": "COP",
                "from": "Discover 3172601889670065",
                "to": "Discover 0720428384694643",
                "description": "Перевод с карты на карту",
            },
            {
                "id": 593027,
                "state": "CANCELED",
                "date": "2023-07-22T05:02:01Z",
                "amount": 30368,
                "currency_name": "Shilling",
                "currency_code": "TZS",
                "from": "Visa 1959232722494097",
                "to": "Visa 6804119550473710",
                "description": "Перевод с карты на карту",
            },
        ]
    )

    data_ex = mock_read_excel

    assert tables_excel("C:/Users/Aleksandr/PycharmProjects/PythonProject/data/transactions_excel_three_str.xlsx") == [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 593027,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
    ]
