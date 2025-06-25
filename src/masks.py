def get_mask_card_number():
    """Функция получения номера карты владельца и выдача его с маской"""
    card_number = str(input())
    if len(card_number) == 16 and card_number.isdigit():
        return print(f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}")
    else:
        return print("Неправильно набран номер карты")


def get_mask_account():
    """Функция получения счета карты владельца и выдача его с маской"""
    account_number = str(input())
    if len(account_number) == 20 and account_number.isdigit():
        return print(f"**{account_number[-4:]}")
    else:
        return print("Неправильно набран номер счета")
