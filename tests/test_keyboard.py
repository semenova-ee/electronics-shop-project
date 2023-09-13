from src.keyboard import Keyboard
from src.item import Item
import pytest

@pytest.fixture
def sample_items():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    return kb

def test_str(sample_items):
    kb = sample_items
    assert str(kb) == 'Dark Project KD87A'

def test_init_lang(sample_items):
    kb = sample_items
    assert str(kb.language) == "EN"

def test_change_lang(sample_items):
    kb = sample_items
    kb.change_lang()
    assert str(kb.language) == "RU"

def test_number_of_sim_raised_exception(sample_items):
    kb = sample_items
    with pytest.raises(AttributeError) as excinfo:
        kb.language = 'CH'
    assert str(excinfo.value) == "property 'language' of 'Keyboard' object has no setter"