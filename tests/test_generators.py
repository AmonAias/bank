import pytest
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator
)


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "operationAmount": {"amount": "100", "currency": {"code": "USD"}},
            "description": "Оплата услуг"
        },
        {
            "id": 2,
            "operationAmount": {"amount": "200", "currency": {"code": "RUB"}},
            "description": "Перевод"
        },
        {
            "id": 3,
            "operationAmount": {"amount": "300", "currency": {"code": "USD"}},
            "description": "Покупка"
        },
    ]
@pytest.mark.parametrize(
    "currency, expected_count",
    [
        ("USD", 2),
        ("RUB", 1),
        ("EUR", 0),
    ]
)
def test_filter_by_currency(sample_transactions, currency, expected_count):
    result = list(filter_by_currency(sample_transactions, currency))
    assert len(result) == expected_count
def test_transaction_descriptions(sample_transactions):
    result = list(transaction_descriptions(sample_transactions))
    assert result == ["Оплата услуг", "Перевод", "Покупка"]


def test_transaction_descriptions_empty():
    result = list(transaction_descriptions([]))
    assert result == []
def test_card_number_generator_basic():
    result = list(card_number_generator(1, 3))
    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
    ]
@pytest.mark.parametrize("num", [1, 10, 999999])
def test_card_number_format(num):
    card = next(card_number_generator(num, num))
    assert len(card) == 19  # 16 цифр + 3 пробела
    assert card.count(" ") == 3
def test_card_number_generator_stop():
    gen = card_number_generator(5, 5)
    assert next(gen) == "0000 0000 0000 0005"
    with pytest.raises(StopIteration):
        next(gen)
