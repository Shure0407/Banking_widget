def filter_by_state(transactions, state):
    """ Функция принимает список операций по карте и
    возвращает новый список выполненных операций, с заданным состоянием """

    executed_transactions = []
    for transaction in transactions:
        if transaction.get("state") and state != "":
            if transaction["state"] == state:
                executed_transactions.append(transaction)
        else:
            if transaction["state"] == "EXECUTED":
                executed_transactions.append(transaction)

    return executed_transactions


def sort_by_date(transactions, sort):
    """ Функция принимает список операций по карте и
        возвращает список с сортировкой по дате """

    if sort == "ascending_sort":
        sorted_transactions_as = sorted(transactions, key=lambda transaction: transaction['date'])
        return sorted_transactions_as
    elif sort == "descending_sort":
        sorted_transactions_des = sorted(transactions, key=lambda transaction: transaction['date'], reverse=True)
        return sorted_transactions_des
    else:
        sorted_transactions_def = sorted(transactions, key=lambda transaction: transaction['date'], reverse=True)
        return sorted_transactions_def
