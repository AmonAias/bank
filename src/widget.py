from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счёта в зависимости от типа

    Args:
        data: Строка с типом и номером (например "Visa Platinum 7000792289606361")

    Returns:
        Строка с замаскированным номером (например "Visa Platinum 7000 79** **** 6361")
    """
    # Разделение на слова
    parts = data.split()

    # Номер - последний элемент
    number = parts[-1]

    # Тип - все элементы кроме последнего
    account_type = " ".join(parts[:-1])

    if "счет" in account_type.lower():
        return f"{account_type} {get_mask_account(number)}"
    else:
        return f"{account_type} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ

    Args:
        date_str: Строка с датой в формате ISO (например "2024-03-11T02:26:18.671407")

    Returns:
        Строка с датой в формате ДД.ММ.ГГГГ (например "11.03.2024")
    """
    # Разделяем дату и время
    date_part = date_str.split("T")[0]

    # Разбиваем на компоненты
    year, month, day = date_part.split("-")

    return f"{day}.{month}.{year}"