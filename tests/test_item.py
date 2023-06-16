from src.item import Item


def test_item(item):
    item = item[0]
    assert item.name == 'Ноутбук'
    item.name = 'Планшет'
    assert item.name == 'Планшет'
    assert item.price == 1000.0
    assert item.calculate_total_price() == 5000.0
    item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 900.0
    assert len(Item.all) == 2