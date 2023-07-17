from products import Product

class Store:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total_quantity(self):
        total_quantity = sum(product.quantity for product in self.product_list)
        return total_quantity

    def get_all_products(self):
        return [product for product in self.product_list if product.is_active()]

    def order(self, shopping_list):
        total_price = 0.0

        for product_title, quantity in shopping_list:
            found_product = None
            for product in self.product_list:
                if product.name == product_title and product.is_active():
                    found_product = product
                    break

            if found_product is not None:
                if found_product.quantity >= quantity:
                    total_price += found_product.price * quantity
                    found_product.quantity -= quantity
                else:
                    raise Exception(f"Not enough stock for {found_product.name}")
            else:
                raise Exception(f"Product not found in store: {product_title}")

        return total_price

    def get_product_by_title(self, title):
        for product in self.product_list:
            if product.name == title:
                return product
        return None



def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                   ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))

if __name__ == "__main__":
    main()
