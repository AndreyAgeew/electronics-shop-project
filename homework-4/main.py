from src.item import Item
from src.phone import Phone

if __name__ == '__main__':

    # смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    print(str(phone1))
    print(repr(phone1))
    item1 = Item("Смартфон", 10000, 20)
    print(item1 + phone1)
    print(phone1 + phone1)
