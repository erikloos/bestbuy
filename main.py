from products import Product
from store import Store

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)


def start(current_store: Store) -> None:
    while True:
        print_menu()
        command = get_valid_input()

        if command == 1:
            all_products = current_store.get_all_products()
            print_all_products(all_products)

        elif command == 2:
            total_amount = current_store.get_total_quantity()
            print(f"Total of {total_amount} items in store\n")

        elif command == 3:
            order_products(current_store)

        else:
            break


def order_products(current_store: Store) -> None:
    total_price = 0
    while True:
        all_products = current_store.get_all_products()
        if not all_products:
            print("No products to buy available.")
            break
        current_order = get_valid_order(all_products)
        if current_order is None:
            print(f"Your total price is {total_price:.2f}\n")
            break

        try:
            shopping_list = [current_order]
            current_price = current_store.order(shopping_list)
            total_price += current_price
            print(f"This order costs: {current_price:.2f}\n")
        except Exception as e:
            print(f"Purchase failed: {e}")


def get_valid_order(all_products: list[Product]) -> tuple[Product, int] | None:
    while True:
        print("Press Enter on both inputs to finish your order")
        print_all_products(all_products)
        try:
            product_number = input("Which product # do you want? ")
            amount = input("What amount do you want? ")

            if product_number == "" and amount == "":
                return None

            product_number = int(product_number)
            amount = int(amount)
            product = all_products[product_number - 1]
            current_order = (product, amount)
            return current_order

        except IndexError:
            print("Error: The number does not belong to a product\n")
            continue
        except ValueError:
            print("Error: Please enter a valid number\n")
            continue


def print_all_products(all_products: list[Product]) -> None:
    print("Available Products:")
    print("------")
    for index, product in enumerate(all_products, 1):
        item = product.show()
        print(f"{index}. {item}")
    print("------")


def print_menu() -> None:
    print(
        "   Store Menu\n"
        f"   {'-' * 8}\n"
        "1. List all products in store\n"
        "2. Show total amount in store\n"
        "3. Make an order\n"
        "4. Quit")


def get_valid_input() -> int:
    while True:
        try:
            user_command = int(input("Please choose a number: "))
            print()
            if user_command > 4 or user_command <= 0:
                print("Enter a valid number")
                continue
            return user_command
        except ValueError:
            print("Error with your choice! Try again\n")


def main() -> None:
    start(best_buy)


if __name__ == '__main__':
    main()