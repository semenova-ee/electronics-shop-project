from src.exceptions import MyCustomError, InstantiateCSVError
import csv


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
        self.__class__.all.append(self)

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @property
    def name(self):
        """Геттер для свойства name."""
        return self.__name

    @name.setter
    def name(self, value):
        """Сеттер для свойства name."""
        if len(value) > 10:
            raise MyCustomError("Название должно быть не более 10 символов")
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_path: str):
        """
        Инициализирует экземпляры класса Item данными из CSV-файла.

        :param file_path: Путь к CSV-файлу.
        :return: Список экземпляров класса Item.
        """
        items = []
        try:
            with open(file_path, "r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                next(csv_reader)
                for row in csv_reader:
                    if not all(
                            column in csv_reader.fieldnames
                            for column in ["name", "price", "quantity"]
                    ):
                        raise InstantiateCSVError("Файл item.csv поврежден")
                    name = row["name"]
                    price = cls.string_to_number(row["price"])
                    quantity = int(row["quantity"])
                    item = cls(name, price, quantity)
                    items.append(item)
            return items
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(s: str) -> int:
        """
        Получает строку
        Выводит значение в виде целого числа
        """
        return int(float(s))

    def __add__(self, other):
        """
        Складывает экземпляры класса (количество товара в магазине) `Phone` и `Item`
        Выполняет проверку, чтобы нельзя было сложить `Phone` или `Item` с экземплярами не `Phone` или `Item` классов.
        """

        if isinstance(other, Item):
            combined_quantity = self.quantity + other.quantity
            return combined_quantity
        else:
            raise TypeError("Unsupported operand type for +")
