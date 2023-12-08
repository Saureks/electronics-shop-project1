class LanguageMixin:
    def __init__(self):
        self.language = "EN"

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"


class Keyboard:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, new_language):
        self.__language = new_language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'

    def __str__(self):
        return self.__name


if __name__ == '__main__':
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb.language) == "EN"

    kb.language = 'CH'
