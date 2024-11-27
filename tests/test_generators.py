import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def test_filter_by_currency(currency_1, currency_2, currency_3, currency_4, currency_5):
    function_1 = filter_by_currency(transactions, "USD")
    function_2 = filter_by_currency([], "USD")
    function_3 = filter_by_currency(transactions, "RUB")
    assert next(function_1) == currency_1
    assert next(function_1) == currency_2
    assert next(function_2) == currency_3
    assert next(function_3) == currency_4
    assert next(function_3) == currency_5

    with pytest.raises(StopIteration):
        assert next(filter_by_currency(transactions, " "))


def test_transaction_descriptions(
    transaction_1,
    transaction_2,
    transaction_3,
    transaction_4,
    transaction_5,
    transaction_6,
):
    generator_1 = transaction_descriptions(transactions)
    generator_2 = transaction_descriptions([])
    assert next(generator_1) == transaction_1
    assert next(generator_1) == transaction_2
    assert next(generator_1) == transaction_3
    assert next(generator_1) == transaction_4
    assert next(generator_1) == transaction_5
    assert next(generator_2) == transaction_6


def test_card_number_generator(
    card_number_1, card_number_2, card_number_3, card_number_4
):
    generator_1 = card_number_generator(1, 10)
    generator_2 = card_number_generator(10, 1)
    assert next(generator_1) == card_number_1
    assert next(generator_1) == card_number_2
    assert next(generator_1) == card_number_3
    assert next(generator_2) == card_number_4

    with pytest.raises(TypeError):
        assert next(card_number_generator(5, "some_sring"))
        assert next(card_number_generator())
