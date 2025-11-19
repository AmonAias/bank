import pytest
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date


# ------------------------------
# Фикстура
# ------------------------------
@pytest.fixture
def sample_numbers():
    return {
        "card": "7000792289606361",
        "card2": "1596837868705199",
        "account": "73654108430135874305",
    }


# ------------------------------
# Параметризованный тест для маскировки карты
# ------------------------------
@pytest.mark.parametrize(
    "number,expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1596837868705199", "1596 83** **** 5199"),
    ],
)
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


# ------------------------------
# Тест маскировки счета
# ------------------------------
def test_get_mask_account(sample_numbers):
    assert get_mask_account(sample_numbers["account"]) == "**4305"


# ------------------------------
# Параметризованный тест для mask_account_card
# ------------------------------
@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected


# ------------------------------
# Тест преобразования даты
# ------------------------------
@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2020-01-01T10:00:00", "01.01.2020"),
    ],
)
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
