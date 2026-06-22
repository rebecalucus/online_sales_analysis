from product_manager import ProductManager
from product import Product
from cart import Cart

import random

manager = ProductManager()
cart = Cart()

p1 = Product("Led", 3500, 2)
p2 = Product("Soundbar", 250, 5)
p3 = Product("Tastatura", 400, 26)
p4 = Product("Tv", 6500, 3)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)
manager.add_product(p4)

print("Lista produse:")
manager.show_products()

print("\nValoarea totală a inventarului:")
manager.total_value()

def main():
    random_products = random.sample(manager.products, 3)

    for product in random_products:
        cart.add_product(product)

    cart.show_cart()

    total = cart.total_price()
    print(f"Total de plată: {total} lei")

main()
