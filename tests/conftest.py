import pytest
from src.item import Item
import os

@pytest.fixture
def item():
    item = Item('Ноутбук', 1000.0, 5)
    item2 = Item('Компьютер', 1000.0, 5)
    yield item, item2


@pytest.fixture
def path():
    return os.path.abspath("src/items.csv")
