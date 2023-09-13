from src.item import Item
class Phone(Item):
    def __init__(
            self, name: str, price: float, quantity: int, number_of_sim: int
    ) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim


    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sims(self):
        """The number_of_sims property."""
        return self.number_of_sims

    @number_of_sims.setter
    def number_of_sims(self, value):
        if value <= 0:
            raise ValueError(
                "Количество физических SIM-карт должно быть целым числом больше нуля."
            )
        self.number_of_sims = value