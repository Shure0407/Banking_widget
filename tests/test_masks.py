from src import masks


def test_get_mask_card_number():
    assert masks.get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert masks.get_mask_card_number("87000792289606361") == None
    assert masks.get_mask_card_number("f7000792289606361") == None
    assert masks.get_mask_card_number("") == None
    assert masks.get_mask_card_number("asd") == None
    assert masks.get_mask_card_number("700079228f9606361") == None


def test_get_mask_account():
    assert masks.get_mask_account("73657922896000006361") == "**6361"
    assert masks.get_mask_account("173657922896000006361") == None
    assert masks.get_mask_account("736579228d96000006361") == None
    assert masks.get_mask_account("") == None
    assert masks.get_mask_account("qwerty") == None
    assert masks.get_mask_account("99999999999999999999") == "**9999"