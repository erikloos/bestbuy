from products import Product

class Store:

    def __init__(self, products: list[Product]):
        self.product_list = []
        for product in products:
            self.add_product(product)

    def add_product(self, product: Product):
        if product not in self.product_list:
            self.product_list.append(product)


    def remove_product(self, product: Product):
        self.product_list.remove(product)


    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()
        return total_quantity


    def get_all_products(self) -> list[Product]:
        all_products = []
        for product in self.product_list:
            if product.is_active():
                all_products.append(product)
        return all_products


    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        total_price = 0
        for item in shopping_list:
            product = item[0]
            quantity = item[1]
            if product in self.product_list and product.is_active():
                total_price += product.buy(quantity)
        return total_price
