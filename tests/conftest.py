import pytest
from src.item import Item
import os


@pytest.fixture
def item1():
    return Item('Ноутбук', 1000.0, 5)


@pytest.fixture
def item2():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def csv_path():
    return os.path.abspath("src/items.csv")
