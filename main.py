from product_manager import ProductManager
from product import Product

manager = ProductManager()


p1 = Product("Led", 3500, 2)
p2 = Product("Soundbar", 250, 5)
p3 = Product("Tastatura", 400, 26)
p4 = Product("Tv", 6500, 3)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)
manager.add_product(p4)

