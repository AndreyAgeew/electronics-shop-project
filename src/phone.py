from src.item import Item


class Phone(Item):
    """
    Класс, представляющий телефон в магазине.
    Наследует все атрибуты класса Item и добавляет атрибут `sim_slots` для количества поддерживаемых сим-карт.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создает экземпляр класса Phone.

        :param name: Название телефона.
        :param price: Цена за единицу телефона.
        :param quantity: Количество телефонов в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"Phone{self.name, self.price, self.quantity, self.number_of_sim}"

    @property
    def number_of_sim(self) -> int:
        """
        Возвращает количество поддерживаемых сим-карт.

        :return: Количество поддерживаемых сим-карт.
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value) -> None:
        """
        Устанавливает количество физических SIM-карт, поддерживаемых телефоном.

        :param value: Новое значение количества физических SIM-карт.
        :raises: ValueError, если значение меньше или равно нулю.
        """
        if value <= 0:
            raise ValueError("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = value

    def __add__(self, other) -> int:
        """
        Переопределение оператора сложения (+) для Phone и Item.
        Результатом сложения будет суммарное количество товара.

        :param other: Другой объект для сложения (должен быть экземпляром класса Phone или Item).
        :return: суммарное количество товара.
        :raises: TypeError, если other не является экземпляром класса Phone или Item.
        """
        if isinstance(other, (Item, Phone)):
            return self.quantity + other.quantity
        else:
            raise TypeError("Cannot add Phone or Item with object of different type.")

    def __radd__(self, other):
        """Переопределение оператора обратного сложения (+) для Phone и Item."""
        return self.__add__(other)
