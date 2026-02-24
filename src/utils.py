import json

from typing import Any


def load_transactions(path: str) -> Any:
    """Функция которая принимает на вход путь к json файлу и
    возвращает список словарей с данными о финансовых транзакциях"""

    try:
        with open(path, "r", encoding="utf-8") as tr:
            content = tr.read()
            if not content.strip():
                return []
            data = json.loads(content)
            if not isinstance(data, list):
                return []
            return data

    except FileNotFoundError:
        print("Файл не найден:")
        return []


# data_tr = utils.load_transactions('C:/Users/Aleksandr/PycharmProjects/PythonProject/data/operations.json')
