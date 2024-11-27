from typing import Any, Generator


def filter_by_currency(
    list_transaction: list[dict[str, Any]], currency="USD"
) -> Generator[Any, Any, Any]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции"""
    if len(list_transaction) > 0:
        for transaction in list_transaction:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
    else:
        yield "Ошибка ввода"


def transaction_descriptions(
    list_transactions: list[dict[str, Any]]
) -> Generator[Any, Any, Any]:
    """генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    if len(list_transactions) > 0:
        for transaction in list_transactions:
            yield transaction["description"]
    else:
        yield "Ошибка ввода"


def card_number_generator(start: int, stop: int) -> Generator[Any, Any, Any]:
    """Генератор, который выдает номера банковских"""
    if start < stop:
        for number in range(start, stop + 1):
            zero = "0000000000000000"
            number_len = len(str(number))
            card_number = zero[0:-number_len] + str(number)
            yield f"{card_number[0:5]} {card_number[4:9]} {card_number[8:13]} {card_number[12:17]}"
    else:
        yield "Ошибка ввода"


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

# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(2):
#     print(next(usd_transactions))

# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#     print(next(descriptions))

# for card_number in card_number_generator(1, 5):
#    print(card_number)
