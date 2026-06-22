from product import Product

class ProductManager:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            product.display_info()

            if product.quantity == 0:
                print("Stoc insuficient!")

    def total_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity

        print("Valoare totala:", total)

    def remove_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                self.products.remove(product)
                print(f"Produsul '{product.name}' a fost șters.")
                return
        print(f"Produsul '{name}' nu a fost găsit.")