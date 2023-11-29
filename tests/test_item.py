"""Здесь надо написать тесты с использованием pytest для модуля item."""
import unittest

from src.item import Item


class TestItem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Item.instantiate_from_csv()

    def setUp(self):
        Item.all = []

    def test_set_name(self):
        item = Item('Smartphone', 1000, 5)
        self.assertEqual(item.name, 'Smartphone')

        item.name = 'SuperSmart'
        self.assertEqual(item.name, 'SuperSmart')

    def test_calculate_total_price(self):
        item = Item('Smartphone', 1000, 5)
        self.assertEqual(item.calculate_total_price(), 5000)

    def test_string_to_number(self):
        number_string = '10.5'
        number = Item.string_to_number(number_string)
        self.assertEqual(number, 10.5)

    def test_instantiate_from_csv(self):
        Item.instantiate_from_csv()
        self.assertEqual(len(Item.all), 5)
        for item in Item.all:
            self.assertIsInstance(item, Item)
            self.assertIsInstance(item.price, float)
            self.assertIsInstance(item.quantity, int)

    def test_repr(self):
        item = Item('Smartphone', 1000, 5)
        self.assertEqual(repr(item), "Item('Smartphone', 1000, 5)")

    def test_str(self):
        item = Item('Smartphone', 1000, 5)
        self.assertEqual(str(item), 'Smartphone')


if __name__ == '__main__':
    unittest.main()
