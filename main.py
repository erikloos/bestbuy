"""Main module to run the program """

from products import Product
from store import Store

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)


def start(current_store: Store) -> None:
    """Run the store loop and handle the user commands."""
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
    """Handle the order process for a user."""
    shopping_list = []
    while True:
        all_products = current_store.get_all_products()
        if not all_products:
            print("No products to buy available.")
            break
        current_order = get_valid_order(all_products)
        if current_order is None:
            if not shopping_list:
                print("Your shopping cart is empty. No purchase made.")
                break
            try:
                total_price = current_store.order(shopping_list)
                print(f"Your total price is {total_price:.2f}\n")
                break
            except Exception as e:
                print(f"Purchase failed: {e}")
                break

        shopping_list.append(current_order)
        print("Your order was added to your cart\n")




def get_valid_order(all_products: list[Product]) -> tuple[Product, int] | None:
    """Gets and handles the input of the user for a valid product and quantity."""
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
            if product_number <= 0 or amount <= 0:
                print("Please enter a valid number")
                continue

            product = all_products[product_number - 1]
            if product.get_quantity() < amount:
                print("Not enough quantity of this product available")
                continue
            return product, amount

        except IndexError:
            print("Error: The number does not belong to a product\n")
            continue
        except ValueError:
            print("Error: Please enter a valid number\n")
            continue


def print_all_products(all_products: list[Product]) -> None:
    """Print all available products."""
    print("Available Products:")
    print("------")
    for index, product in enumerate(all_products, 1):
        item = product.show()
        print(f"{index}. {item}")
    print("------")


def print_menu() -> None:
    """Print the store menu with the options the user can choose."""
    print(
        "   Store Menu\n"
        f"   {'-' * 8}\n"
        "1. List all products in store\n"
        "2. Show total amount in store\n"
        "3. Make an order\n"
        "4. Quit")


def get_valid_input() -> int:
    """Check the user for a valid menu selection and handles the input."""
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
    """Start the program."""
    start(best_buy)


if __name__ == '__main__':
    main()
