from src.item import Item
from src.phone import Phone
import pytest
from src.exceptions import InstantiateCSVError


@pytest.fixture
def sample_items():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    return item1, item2


def test_calculate_total_price(sample_items):
    """Проверяет подсчет общей суммы"""
    i_1, i_2 = sample_items
    assert i_1.calculate_total_price() == 200000
    assert i_2.calculate_total_price() == 100000


def test_apply_discount(sample_items):
    """Проверяет применение скидки"""
    item1, item2 = sample_items
    item1.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000


def test_all_list_contains_created_items(sample_items):
    """Проверяет количество элементов в Item.all"""
    assert sample_items[0] in Item.all
    assert sample_items[1] in Item.all
    assert len(sample_items) == 2


@pytest.fixture
def csv_file():
    return r"C:\Users\Екатерина\PycharmProjects\electronics-shop-project\src\items1.csv"


def test_instantiate_from_csv(csv_file):
    items = Item.instantiate_from_csv(csv_file)

    # Assert the properties of the instantiated items
    assert len(Item.all) == 10
    assert items[0].name == "samsung"
    assert items[0].price == 1000
    assert items[0].quantity == 3
    assert items[1].name == "apple"
    assert items[1].price == 10
    assert items[1].quantity == 5


def test_string_to_number():
    """Проверяет преобразование str значения в int"""
    assert Item.string_to_number("15.0") == 15
    assert Item.string_to_number("7") == 7


def test_repr(sample_items):
    """Проверяет вывод данных о товаре"""
    item1, item2 = sample_items
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Ноутбук', 20000, 5)"


def test_str(sample_items):
    """Проверяет наименования"""
    item1, item2 = sample_items
    assert str(item1) == 'Смартфон'
    assert str(item2) == 'Ноутбук'


@pytest.fixture
def csv_file_corrupted():
    return r"C:\Users\Екатерина\PycharmProjects\electronics-shop-project\src\items2.csv"


# Define a fixture for a non-existent CSV file
@pytest.fixture
def non_existent_csv_file(tmp_path):
    csv_file_path = tmp_path / "non_existent.csv"
    return csv_file_path


# Test case for a CSV file with missing columns
def test_instantiate_from_csv_missing_columns(csv_file_corrupted):
    """Проверяет выпадение ошибки при использовании поврежденного файла"""
    with pytest.raises(InstantiateCSVError) as exc_info:
        Item.instantiate_from_csv(csv_file_corrupted)
    assert str(exc_info.value) == "Файл item.csv поврежден"


# Test case for a non-existent CSV file
def test_instantiate_from_csv_non_existent(non_existent_csv_file):
    """Проверяет выпадение ошибки при использовании отстутствующего файла"""
    with pytest.raises(FileNotFoundError) as exc_info:
        Item.instantiate_from_csv(non_existent_csv_file)
    assert str(exc_info.value) == "Отсутствует файл item.csv"


@pytest.fixture
def sample_items_phone():
    """Проверяет вывод данных об экзмеплярах классов Item и Phone"""
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    return item1, phone1


def test_repr_phone(sample_items_phone):

    item1, phone1 = sample_items_phone
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str_phone(sample_items_phone):
    """Проверяет вывод наименований"""
    item1, phone1 = sample_items_phone
    assert str(item1) == 'Смартфон'
    assert str(phone1) == 'iPhone 14'


def test_number_of_sim(sample_items_phone):
    """Проверяет вывод количества сим-карт телефона"""
    _, phone1 = sample_items_phone
    assert phone1.number_of_sim == 2


def test_add(sample_items_phone):
    """Проверяет результат сложения экземпляров класса (количество товара в магазине) `Phone` и `Item`"""
    item1, phone1 = sample_items_phone
    assert phone1 + phone1 == 10
    assert item1 + phone1 == 25
