def filter_by_currency(transactions: list[dict], currency: str):
    """
    Фильтрует транзакции по валюте. Возвращает итератор.

    :param transactions: список транзакций
    :param currency: требуемая валюта (например, "USD")
    :return: итератор транзакций
    """
    for item in transactions:
        if item.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield item


def transaction_descriptions(transactions: list[dict]):
    """
    Генератор, возвращающий описания транзакций по очереди.

    :param transactions: список транзакций
    """
    for item in transactions:
        yield item.get("description")


def card_number_generator(start: int, stop: int):
    """
    Генератор номеров банковских карт.

    :param start: начало диапазона (включительно)
    :param stop: конец диапазона (включительно)
    """
    for num in range(start, stop + 1):
        yield f"{num:016d}"[:4] + " " + f"{num:016d}"[4:8] + " " + \
              f"{num:016d}"[8:12] + " " + f"{num:016d}"[12:]
