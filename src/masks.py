def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    if len(card_number) == 16:
        return (
            card_number[0:4]
            + " "
            + card_number[4:6]
            + "**"
            + " "
            + "****"
            + " "
            + card_number[12:]
        )
    return ""


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    if len(account_number) == 20:
        return "**" + account_number[16:]
    return ""


# print(get_mask_card_number("7000792289606361"))
# print(get_mask_account("73654108430135874305"))
