from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        # Создание экземпляра класса Phone.
        # name: Название смартфона.
        # price: Цена за единицу смартфона.
        # quantity: Количество смартфонов в магазине.
        # number_of_sim: Количество поддерживаемых сим-карт.

        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        # Возвращает описание экземпляра класса.
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        if isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            raise TypeError("Неподдерживаемая операция сложения для Phone и данного типа объекта.")

    def __radd__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        elif isinstance(other, Phone):
            raise TypeError("Нельзя сложить Phone с другим экземпляром Phone.")
        else:
            raise TypeError("Неподдерживаемая операция сложения для Phone и данного типа объекта.")

    def __str__(self):
        return self.name
