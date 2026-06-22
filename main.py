from product_manager import ProductManager
from product import Product

manager = ProductManager()


p1 = Product("Laptop", 3500, 2)
p2 = Product("Mouse", 250, 5)
p3 = Product("Tastatura", 400, 3)
p4 = Product("Tv", 6500, 0)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)
manager.add_product(p4)

print("Lista produse:")
manager.show_products()

print("\nValoarea totală a inventarului:")
manager.total_value()