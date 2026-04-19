"""Class for products in the program."""

class Product:
    """Represents a product with its name, price, quantity and status."""

    def __init__(self, name: str, price: float, quantity: int):
        """Initialize a product with parameter name, price and quantity"""
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
        """Return the current quantity of a product."""
        return self.quantity


    def set_quantity(self, quantity: int):
        """Set the quantity of a product and set update status if necessary.
        Deactivates a product if it has 0 quantity."""
        if quantity < 0:
            raise Exception("Quantity can not be negative")
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()
        else:
            self.activate()


    def is_active(self) -> bool:
        """Return whether product is active or not."""
        return self.active


    def activate(self) -> None:
        """Activate a product."""
        self.active = True


    def deactivate(self) -> None:
        """Deactivate a product."""
        self.active = False


    def show(self) -> str:
        """Return a string with parameters of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity: int) -> float:
        """Purchase a product and update the quantity. Return the price of the purchase."""
        if quantity <= 0:
            raise Exception("Need a valid quantity for purchase")
        new_quantity = self.quantity - quantity
        if new_quantity < 0:
            raise Exception("Not enough quantity.")
        self.set_quantity(new_quantity)
        price = self.price * quantity
        return float(price)
