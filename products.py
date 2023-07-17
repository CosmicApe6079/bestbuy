class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

    def purchase(self, purchase_quantity):
        if purchase_quantity > self.quantity:
            raise ValueError("Insufficient quantity")
        self.quantity -= purchase_quantity
        return f"You purchased {purchase_quantity} units of {self.name}."

    def get_quantity(self):
        return float(self.quantity)

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if not self.active or quantity <= 0 or quantity > self.quantity:
            raise Exception("Invalid purchase")

        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        return total_price

