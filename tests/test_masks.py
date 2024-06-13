import pytest

from src.masks import mask_card_number, convert_date


@pytest.mark.parametrize("x, expected", [("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"), (
        "Maestro 7000 7922 8960 6361", "Maestro 7000 79** **** 6361"),
                                         ("Счет 73654108430135874305", "Счет **4305")])
def test_add(x, expected):
    assert mask_card_number(x) == expected


@pytest.mark.parametrize("x, expected", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def teste_dated(x, expected):
    assert convert_date(x) == expected
