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

class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def set_quantity(self, quantity):
        if quantity != 0:
            raise ValueError("Non-stocked products should have a quantity of 0.")
        super().set_quantity(0)

    def purchase(self, purchase_quantity):
        raise ValueError("Non-stocked products cannot be purchased.")


class LimitedProduct(Product):
    def __init__(self, name, price, max_quantity):
        super().__init__(name, price, max_quantity)
        self.max_quantity = max_quantity

    def set_quantity(self, quantity):
        if quantity > self.max_quantity:
            raise ValueError("Quantity exceeds the maximum allowed quantity.")
        super().set_quantity(quantity)

    def purchase(self, purchase_quantity):
        if purchase_quantity > self.max_quantity:
            raise ValueError("Exceeded maximum allowed quantity.")
        super().purchase(purchase_quantity)

