from typing import Any


def filter_by_currency(transactions: Any, currency: str) -> Any:
    """Функция принимает на вход список словарей, представляющих транзакции и
      возвращает итератор транзакций, где валюта операций соответствует заданной"""

    return (transaction for transaction in transactions if currency in transaction[
        "operationAmount"]["currency"]["name"])


def transaction_descriptions(transactions: Any) -> Any:
    """Функция принимает на вход список словарей, представляющих транзакции и
                  возвращает описание каждой операции по очереди"""

    for transaction in transactions:
        yield transaction['description']
#    return (transaction["description"] for transaction in transactions)


def card_number_generator(start: int = 1, stop: int = 9999999999999999) -> Any:
    """Функция генератор, который выдает номера банковских карт"""

    for number in range(start, stop + 1):
        yield (f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " "
               + f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:16])
