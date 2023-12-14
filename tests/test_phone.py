import unittest
from src.phone import Phone
from src.item import Item


class TestPhone(unittest.TestCase):
    def setUp(self):
        self.phone1 = Phone("iPhone 14", 120000, 5, 2)
        self.phone2 = Phone("Samsung Galaxy", 100000, 3, 1)
        self.item1 = Item("Nokia", 10000, 20)

    def test_attributes(self):
        self.assertEqual(self.phone1.name, 'iPhone 14')
        self.assertEqual(self.phone1.price, 120000)
        self.assertEqual(self.phone1.quantity, 5)
        self.assertEqual(self.phone1.number_of_sim, 2)

    def test_repr(self):
        self.assertEqual(repr(self.phone1), "Phone('iPhone 14', 120000, 5, 2)")

    def test_add_phone_item(self):
        with self.assertRaises(TypeError):
            result = self.phone1 + self.item1

    def test_add_phones(self):
        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        phone2 = Phone("Samsung Galaxy", 100_000, 3, 1)

        result = phone1 + phone2
        self.assertEqual(result, 8)

    def test_add_invalid_types(self):
        with self.assertRaises(TypeError):
            result = self.phone1 + "SomeString"
