from src.item import Item


def test_item(item, path):
    item = item[0]
    assert item.name == 'Ноутбук'
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    assert item.price == 1000.0
    assert item.calculate_total_price() == 5000.0
    item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 900.0
    assert len(Item.all) == 2
    Item.instantiate_from_csv(path)
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
