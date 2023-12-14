import unittest
from src.keyboard import Keyboard, Mixin


class TestKeyboard(unittest.TestCase):
    def setUp(self):
        self.kb = Keyboard('Dark Project KD87A', 9600, 5)

    def test_str(self):
        self.assertEqual(str(self.kb), "Dark Project KD87A")

    def test_language(self):
        self.assertEqual(str(self.kb.language), "EN")

    def test_change_lang(self):
        self.kb.change_lang()
        self.assertEqual(str(self.kb.language), "RU")

        self.kb.change_lang()
        self.assertEqual(str(self.kb.language), "EN")


class TestLanguageMixin(unittest.TestCase):
    def setUp(self):
        self.lang_mixin = Mixin()

    def test_init(self):
        self.assertEqual(self.lang_mixin.language, "EN")

    def test_change_lang(self):
        self.lang_mixin.change_lang()
        self.assertEqual(self.lang_mixin.language, "RU")

        self.lang_mixin.change_lang()
        self.assertEqual(self.lang_mixin.language, "EN")


if __name__ == '__main__':
    unittest.main()
