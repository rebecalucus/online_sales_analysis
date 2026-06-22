class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product):
        self.cart_items.append(product)

    def total_price(self):
        total = 0
        for product in self.cart_items:
            total += product.price
        return total
    
    def show_cart(self):
           if not self.cart_items:
                print("Cosul este  gol")
                return
           
           print("Produse în coș:")
           for produs in self.cart_items:
                print(f"- {produs.name}: {produs.price} lei")
