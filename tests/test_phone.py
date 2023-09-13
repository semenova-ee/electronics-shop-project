from src.item import Item
from src.phone import Phone
import pytest


@pytest.fixture
def sample_items():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    return item1, phone1


def test_repr_phone(sample_items):
    """Проверяет вывод данных об экзмеплярах классов Item и Phone"""
    item1, phone1 = sample_items
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str_phone(sample_items):
    """Проверяет вывод наименований"""
    item1, phone1 = sample_items
    assert str(item1) == 'Смартфон'
    assert str(phone1) == 'iPhone 14'


def test_number_of_sim(sample_items):
    """Проверяет вывод количества сим-карт телефона"""
    _, phone1 = sample_items
    assert phone1.number_of_sim == 2


def test_add(sample_items):
    """Проверяет результат сложения экземпляров класса (количество товара в магазине) `Phone` и `Item`"""
    item1, phone1 = sample_items
    assert phone1 + phone1 == 10
    assert item1 + phone1 == 25
