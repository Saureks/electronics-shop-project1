from src.item import Item


class Mixin:
    __language = "EN"

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

    @property
    def language(self):
        return self.__language


class Keyboard(Item, Mixin):
    pass

    #
    # @language.setter
    # def change_lang(self, new_language):
    #     if new_language in ["EN", "RU"]:
    #         self.language = new_language
    #     raise AttributeError("property 'language' of 'Keyboard' object has no setter")
