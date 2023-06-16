class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.all.append(self)

    @property
    def name(self) -> str:
        """
        Получает название товара.

        :return: Название товара.
        """
        return self.__name

    @name.setter
    def name(self, value) -> None:
        """
        Устанавливает название товара.

        :param value: Новое название товара.
        """
        self.__name = value

    @property
    def price(self) -> float:
        """
        Получает цену за единицу товара.

        :return: Цена за единицу товара.
        """
        return self.__price

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.__quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.__price *= self.pay_rate
