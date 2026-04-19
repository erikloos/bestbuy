class Product:


    def __init__(self, name: str, price: float, quantity: int):
        self.active = True
        if not name:
            raise Exception("Name can not be empty")
        self.name = name
        if price < 0:
            raise Exception("Price can not be negative")
        self.price = price
        if quantity < 0:
            raise Exception("Quantity can not be negative")
        self.quantity = quantity


    def get_quantity(self) -> int:
        return self.quantity


    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise Exception("Quantity can not be negative")
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()
        else:
            self.activate()


    def is_active(self) -> bool:
        return self.active


    def activate(self) -> None:
        self.active = True


    def deactivate(self) -> None:
        self.active = False


    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise Exception("Need a valid quantity for purchase")
        new_quantity = self.quantity - quantity
        if new_quantity < 0:
            raise Exception("Not enough quantity.")
        self.set_quantity(new_quantity)
        price = self.price * quantity
        return float(price)
