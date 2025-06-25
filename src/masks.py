def get_mask_card_number(account_or_card):
    """Функция получения номера карты владельца и выдача его с маской"""

    if len(account_or_card) == 16 and account_or_card.isdigit():
        card_number = f"{account_or_card[0:4]} {account_or_card[4:6]}** **** {account_or_card[-4:]}"
        return card_number
    else:
        return print("Неправильно набран номер карты")


def get_mask_account(account_or_card):
    """Функция получения счета карты владельца и выдача его с маской"""

    if len(account_or_card) == 20 and account_or_card.isdigit():
        account_number = f"**{account_or_card[-4:]}"
        return account_number
    else:
        return print("Неправильно набран номер счета")
