from product import Product

class ProductManager:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            product.display_info()
    def total_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity

        print("Valoare totala:", total)