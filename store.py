"""Class for stores in the program."""

from products import Product

class Store:
    """Represents a store that manages a collection of products."""

    def __init__(self, products: list[Product]):
        """Initialize a store with a list of products."""

        self.product_list = []
        for product in products:
            self.add_product(product)

    def add_product(self, product: Product):
        """Add a product to the store, if it is not already in the store,"""
        if product not in self.product_list:
            self.product_list.append(product)


    def remove_product(self, product: Product):
        """Remove a product from the store"""
        self.product_list.remove(product)


    def get_total_quantity(self) -> int:
        """Return the total amount of quantity of a product in the store."""
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()
        return total_quantity


    def get_all_products(self) -> list[Product]:
        """Return all active products of the store in a list."""
        all_products = []
        for product in self.product_list:
            if product.is_active():
                all_products.append(product)
        return all_products


    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """Purchase a shopping list and return the total price of it.
        Sums up the quantity of the product in shopping list and checks,
        if the quantity of the product is available.
        Update the quantity of each product."""
        total_price = 0
        quantities_by_product = {}

        # Collect quantity for each product
        for item in shopping_list:
            product = item[0]
            quantity = item[1]
            if product not in quantities_by_product:
                quantities_by_product[product] = quantity
            else:
                quantities_by_product[product] += quantity

        # Validate if product has enough quantity and is available
        for product, quantity in quantities_by_product.items():
            if product in self.product_list and product.is_active():
                if product.get_quantity() < quantity:
                    raise Exception("Not enough quantity of product available")
                if quantity <= 0:
                    raise Exception("Enter a valid quantity")
            else:
                raise Exception("Product is not available")

        # Buy each product and changes its quantity
        for product, quantity in quantities_by_product.items():
            total_price += product.buy(quantity)
        return total_price
