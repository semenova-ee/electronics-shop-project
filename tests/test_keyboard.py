from src.keyboard import Keyboard
import pytest


@pytest.fixture
def sample_items():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb


def test_str(sample_items):
    """Проверяет вывод наименования клавиатуры"""
    kb = sample_items
    assert str(kb) == 'Dark Project KD87A'


def test_init_lang(sample_items):
    """Проверяет язык на клавиатуре"""
    kb = sample_items
    assert str(kb.language) == "EN"


def test_change_lang(sample_items):
    """Проверяет измнение языка"""
    kb = sample_items
    kb.change_lang()
    assert str(kb.language) == "RU"


def test_number_of_sim_raised_exception(sample_items):
    """Проверяет возникновние ошибки при использовании неподдерживаемого языка"""
    kb = sample_items
    with pytest.raises(AttributeError) as excinfo:
        kb.language = 'CH'
    assert str(excinfo.value) == "property 'language' of 'Keyboard' object has no setter"
