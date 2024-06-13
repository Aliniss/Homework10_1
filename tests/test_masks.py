import pytest

from src.masks import mask_card_number

@pytest.mark.parametrize("cards", [('Visa Platinum 7000 7922 8960 6361')])
def test_mask_card_number(cards):
    assert mask_card_number(cards)
