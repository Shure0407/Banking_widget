from typing import Any

from src import masks


def test_get_mask_card_number() -> Any:
    """Тестирование функции получения номера карты владельца и выдача его с маской"""

    assert masks.get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert masks.get_mask_card_number("87000792289606361") is None
    assert masks.get_mask_card_number("f7000792289606361") is None
    assert masks.get_mask_card_number("") is None
    assert masks.get_mask_card_number("asd") is None
    assert masks.get_mask_card_number("700079228f9606361") is None


def test_get_mask_account() -> Any:
    """Тестирование функции получения счета карты владельца и выдача его с маской"""

    assert masks.get_mask_account("73657922896000006361") == "**6361"
    assert masks.get_mask_account("173657922896000006361") is None
    assert masks.get_mask_account("736579228d96000006361") is None
    assert masks.get_mask_account("") is None
    assert masks.get_mask_account("qwerty") is None
    assert masks.get_mask_account("99999999999999999999") == "**9999"
