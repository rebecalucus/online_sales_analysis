class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Produs: {self.name}")
        print(f"Pret: {self.price} lei")
        print(f"Cantitate: {self.quantity}")
        
    def update_quantity(self, amount):
        if amount < 0:
            if self.quantity >= -amount:
                self.quantity += amount
                print(f"Stoc actualizat: {self.quantity}")
            else:
                print("Nu exista stoc suficient!")
        else:
            self.quantity += amount
            print(f"Stoc actualizat: {self.quantity}")