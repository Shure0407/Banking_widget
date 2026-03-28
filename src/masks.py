import logging
from typing import Any

masks_logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")

masks_logger.addHandler(file_handler)
file_handler.setFormatter(file_formatter)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(account_or_card: Any) -> Any:


    """Функция получения номера карты владельца и выдача его с маской"""

    if len(account_or_card) == 16 and account_or_card.isdigit():
        card_number = f"{account_or_card[0:4]} {account_or_card[4:6]}** **** {account_or_card[-4:]}"
        masks_logger.info("Выдача номера карты с маской")
        return card_number
    else:
        masks_logger.error("Неправильно введен номер карты")
        return print("Неправильно набран номер карты")



def get_mask_account(account_or_card: Any) -> Any:



    """Функция получения счета карты владельца и выдача его с маской"""

    if len(account_or_card) == 20 and account_or_card.isdigit():
        account_number = f"**{account_or_card[-4:]}"
        masks_logger.info("Выдача счета карты с маской")
        return account_number
    else:
        masks_logger.error("Неправильно введен номер счета")
        return print("Неправильно набран номер счета")
