import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number):
    assert get_mask_card_number("7000792289606361") == card_number

    with pytest.raises(AssertionError):
        assert get_mask_card_number("70007922896063611111")
        assert get_mask_card_number("12345")
        assert get_mask_card_number(" ")


def test_get_mask_account(mask_account):
    assert get_mask_account("73654108430135874305") == mask_account

    with pytest.raises(AssertionError):
        assert get_mask_account("736541084301358743055555")
        assert get_mask_account("12345")
        assert get_mask_account(" ")
