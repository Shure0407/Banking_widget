from src import widget

import pytest


def test_get_date():
    assert widget.get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert widget.get_date("2024:03:11T02:26:18.671407") == "11.03.2024"
    assert widget.get_date("2024::11T02:26:18.671407") is None
    assert widget.get_date("2024:RH:11T02:26:18.671407") is None
    assert widget.get_date("20OO:03:11T02:26:18.671407") is None
    assert widget.get_date("2024:R03:LKT02:26:18.671407") is None
    assert widget.get_date("2024-03-11T0") is None
    assert widget.get_date("2024:03:11TAS:DF:FG.671407") == "11.03.2024"


@pytest.mark.parametrize('account, expected', [
    ('Счет 70007000092289606361','Счет  **6361'),
    ("Счет 170007000092289606361", None),
    ("Счет 0007000092289606361", None),
    ("70007000092289606361", " **6361"),
    ("", None),
    ("Visa Platinum 7000792289606361","Visa Platinum  7000 79** **** 6361"),
    ("Visa Platinum 17000792289606361",None),
    ("Visa Platinum 000792289606361",None),
    ("7000792289606361"," 7000 79** **** 6361")
])

def test_mask_account_card(account, expected):
    assert widget.mask_account_card(account) == expected
#    assert widget.mask_account_card("Счет 170007000092289606361") is None
#    assert widget.mask_account_card("Счет 0007000092289606361") is None
#    assert widget.mask_account_card("70007000092289606361") == "**6361"
#    assert widget.mask_account_card("") is None

#   assert widget.mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum  7000 79** **** 6361"
#  assert widget.mask_account_card("Visa Platinum 17000792289606361") is None
#    assert widget.mask_account_card("Visa Platinum 000792289606361") is None
#    assert widget.mask_account_card("7000792289606361") == "7000 79** **** 6361"

