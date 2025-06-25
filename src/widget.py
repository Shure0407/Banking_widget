from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_details):
    """Функция приема строки с номером карты или счетом владельца и выдача его с соответствующей маской"""

    pay_system = "".join(char for char in account_details if char.isalpha() or char.isspace())
    account_or_card = "".join(char for char in account_details if char.isdigit())

    if len(account_or_card) == 16:
        print(f"{pay_system} {get_mask_card_number(account_or_card)}")
    elif len(account_or_card) == 20:
        print(f"{pay_system} {get_mask_account(account_or_card)}")
    else:
        print("Проверьте правильность введенного номера")


def get_gate(time_event):
    """Функция выделения даты из временного события"""

    date_format = f"{time_event[8:10]}.{time_event[5:7]}.{time_event[0:4]}"
    return date_format
