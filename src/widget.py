from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_account: str) -> str:
    """Функция, которая обрабатывает информацию о картах и счетах"""
    if "Счет" in bank_account:
        bank_account_account = get_mask_account(bank_account[5:])
        return f"Счет {bank_account_account}"
    elif "Maestro" in bank_account:
        bank_account_card = get_mask_card_number(bank_account[8:])
        return f"Maestro {bank_account_card}"
    elif "MasterCard" in bank_account:
        bank_account_card = get_mask_card_number(bank_account[11:])
        return f"MasterCard {bank_account_card}"
    elif "Visa Classic" in bank_account:
        bank_account_card = get_mask_card_number(bank_account[13:])
        return f"Visa Classic {bank_account_card}"
    elif "Visa Platinum" in bank_account:
        bank_account_card = get_mask_card_number(bank_account[14:])
        return f"Visa Platinum {bank_account_card}"
    elif "Visa Gold" in bank_account:
        bank_account_card = get_mask_card_number(bank_account[10:])
        return f"Visa Gold {bank_account_card}"
    return ""


# print(mask_account_card('Счет 64686473678894779589'))
# print(mask_account_card('Счет 35383033474447895560'))
# print(mask_account_card('Счет 73654108430135874305'))
# print(mask_account_card('Maestro 1596837868705199'))
# print(mask_account_card('MasterCard 7158300734726758'))
# print(mask_account_card('Visa Classic 6831982476737658'))
# print(mask_account_card('Visa Platinum 8990922113665229'))
# print(mask_account_card('Visa Gold 5999414228426353'))


def get_date(date_today: str) -> str:
    """Функция, которая принимает на вход строку с датой"""
    if len(date_today) == 26:
        day = int(date_today[8:10])
        month = int(date_today[5:7])
        year = int(date_today[0:4])
        if 1 <= day <= 9 and 1 <= month <= 9 and 2000 <= year <= 2500:
            return f"0{day}.0{month}.{year}"
        elif 10 <= day <= 31 and 10 <= month <= 12 and 2000 <= year <= 2500:
            return f"{day}.{month}.{year}"
    return ""


# print(get_date('2024-03-11T02:26:18.671407'))
