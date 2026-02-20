from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_details: Any) -> Any:
    """Функция приема строки с номером карты или счетом владельца и выдача его с соответствующей маской"""

    pay_system = "".join(char for char in account_details if char.isalpha() or char.isspace())
    account_or_card = "".join(char for char in account_details if char.isdigit())

    if len(account_or_card) == 16:
        return f"{pay_system} {get_mask_card_number(account_or_card)}"
    elif len(account_or_card) == 20:
        return f"{pay_system} {get_mask_account(account_or_card)}"
    else:
        return print("Проверьте правильность введенного номера")


def get_date(time_event: Any) -> Any:
    """Функция выделения даты из временного события"""

    if (len(time_event) == 26 and time_event[0:4].isdigit() and time_event[5:7].isdigit()
            and time_event[8:10].isdigit()):
        date_format = f"{time_event[8:10]}.{time_event[5:7]}.{time_event[0:4]}"
        return date_format
    else:
        return print("Проверьте правильность формата")
