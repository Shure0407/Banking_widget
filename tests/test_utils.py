from src import utils


def test_load_transactions(path) -> list[dict] | None:
    """Тестирование функции, которая принимает на вход путь к json файлу и
    возвращает список словарей с данными о финансовых транзакциях"""

    assert utils.load_transactions("C:/Users/Aleksandr/PycharmProjects/PythonProject/data/123.json") == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
    ]

    assert (
        utils.load_transactions("C:/Users/Aleksandr/PycharmProjects/PythonProject/data/12.json") == []
    )  # ошибка имени файла
    assert (
        utils.load_transactions("C:/Users/Aleksandr/PycharmProjects/PythonProject/data/11.json") == []
    )  # неверный формат данных
    assert (
        utils.load_transactions("C:/Users/Aleksandr/PycharmProjects/PythonProject/data/1.json") == []
    )  # отсутствуют данные
