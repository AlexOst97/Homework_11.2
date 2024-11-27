from typing import Any


def filter_by_state(
    list_of_dictionaries: list[dict[str, Any]], keyword="EXECUTED"
) -> list[dict[str, Any]]:
    """Вывод функции со статусом по умолчанию 'EXECUTED'"""
    answer_status = []
    for list_status in list_of_dictionaries:
        if list_status["state"] == keyword:
            answer_status.append(list_status)
    return answer_status


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ]
    )
)


def sort_by_date(
    enter_date: list[dict[str, Any]], reverse=True
) -> list[dict[str, Any]]:
    """Вывод функции (сортировка по убыванию, т. е. сначала самые последние операции)"""
    list_operation = sorted(
        enter_date, key=lambda list_new: list_new["date"], reverse=reverse
    )
    return list_operation


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ]
    )
)
