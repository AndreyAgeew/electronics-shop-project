import pytest
from src.item import Item


@pytest.fixture
def item():
    item = Item('Ноутбук', 1000.0, 5)
    item2 = Item('Ноутбук', 1000.0, 5)
    yield item, item2
