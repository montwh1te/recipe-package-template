class Ingredients:
    def __init__(self, nome, quantity, unit):
        self.name = nome
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.name}"