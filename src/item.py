import csv
import os


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
        self.price = price
        self.quantity = quantity
        Item.all.append(self)  # Добавлякм экземпляр в список all

    @property
    def name(self):
        """Возвращает полное имя сотрудника. К атрибуту можно обращаться без ()."""
        return self.__name

    @name.setter
    def name(self, name):
        """Метод срабатывает при операции присваивания."""
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        price = self.price * self.quantity
        return price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, self):
        file_path = os.path.join(os.path.dirname(__file__), '../src/items.csv')
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv.
        """
        cls.all.clear()
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name'][:10]
                price = float(row['price'])
                quantity = self.string_to_number(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        """
        Возвращает число из числа-строки.

        :param string: Число в виде строки.
        :return: Число.
        """
        return int(float(string))

    def __repr__(self):
        """
        Возвращает описание экземплора класса.
        """
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает строковое предоставление экземпляра класса.
            """
        return self.__name


if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
