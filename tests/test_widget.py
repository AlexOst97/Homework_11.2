import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(account_card):
    assert mask_account_card("Счет 64686473678894779589") == account_card
    assert mask_account_card("Счет 35383033474447895560") == "Счет **5560"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert (
        mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    )
    assert (
        mask_account_card("MasterCard 7158300734726758")
        == "MasterCard 7158 30** **** 6758"
    )
    assert (
        mask_account_card("Visa Classic 6831982476737658")
        == "Visa Classic 6831 98** **** 7658"
    )
    assert (
        mask_account_card("Visa Platinum 8990922113665229")
        == "Visa Platinum 8990 92** **** 5229"
    )
    assert (
        mask_account_card("Visa Gold 5999414228426353")
        == "Visa Gold 5999 41** **** 6353"
    )

    with pytest.raises(AssertionError):
        assert mask_account_card(" ")
    with pytest.raises(AssertionError):
        assert mask_account_card("123")


def test_get_date(date):
    assert get_date("2024-06-05T02:26:18.671407") == date
    assert get_date("2024-11-20T02:26:18.671407") == "20.11.2024"

    with pytest.raises(AssertionError):
        assert get_date(" ")
    with pytest.raises(AssertionError):
        assert get_date("123")
    with pytest.raises(AssertionError):
        assert get_date("2024-11-99T02:26:18.671407")
    with pytest.raises(AssertionError):
        assert get_date("2024-99-20T02:26:18.671407")
