def filter_by_state(transactions: list[dict], state: tuple[()]) -> list[dict]:
    """Функция принимает список операций по карте и
    возвращает новый список выполненных операций, с заданным состоянием"""

    executed_transactions = []
    for transaction in transactions:
        if transaction.get("state") and state != "":
            if transaction["state"] == state:
                executed_transactions.append(transaction)
        else:
            if transaction["state"] == "EXECUTED":
                executed_transactions.append(transaction)

    return executed_transactions


def sort_by_date(transactions: list[dict], sort: tuple[()]) -> list[dict]:
    """Функция принимает список операций по карте и
    возвращает список с сортировкой по дате"""

    if sort == "ascending_sort":
        sorted_transactions_asc = sorted(transactions, key=lambda transaction: transaction["date"])
        return sorted_transactions_asc
    elif sort == "descending_sort":
        sorted_transactions_desc = sorted(transactions, key=lambda transaction: transaction["date"], reverse=True)
        return sorted_transactions_desc
    else:
        sorted_transactions_def = sorted(transactions, key=lambda transaction: transaction["date"], reverse=True)
        return sorted_transactions_def
