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
