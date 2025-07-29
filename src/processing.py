def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список операций по статусу

    :param data: Список словарей с операциями
    :param state: Статус для фильтрации (по умолчанию 'EXECUTED')
    :return: Отфильтрованный список операций
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список операций по дате

    :param data: Список словарей с операциями
    :param reverse: Порядок сортировки (True - по убыванию, False - по возрастанию)
    :return: Отсортированный список операций
    """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)