from src.item import Item


class KeyboardMixin:
    def __init__(self, language="EN"):
        self._language = language

    def change_lang(self):
        """
        Меняет язык с EN на RU и наоборот
        """
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"

    @property
    def language(self):
        return self._language


class Keyboard(Item, KeyboardMixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self._language = "EN"
