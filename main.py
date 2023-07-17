from bestbuy import products, store, promotions
from products import Product as BaseProduct
from store import Store


def start(store_obj):
    while True:
        print("Welcome to the Store!")
        print("Please select an option:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("All products in store:")
            all_products = store_obj.get_all_products()
            for product in all_products:
                print(product.name)
            print()

        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print("Total amount in store:", total_quantity)
            print()

        elif choice == "3":
            shopping_list = []
            while True:
                product_title = input("Enter the product title (or 'done' to finish): ")
                if product_title == "done":
                    break
                quantity = int(input("Enter the quantity: "))
                product = store_obj.get_product_by_title(product_title)
                if product is None:
                    print("Product not found in store.")
                else:
                    shopping_list.append((product, quantity))
            try:
                total_price = store_obj.order(shopping_list)
                print("Order placed successfully.")
                print("Total price:", total_price)
            except Exception as e:
                print("Order failed:", str(e))

        elif choice == "4":
            print("Quitting...")
            break

        else:
            print("Invalid choice. Please try again.")

        print()

if __name__ == "__main__":
    # Setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, max_quantity=1)
                    ]
    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)
    start(best_buy)

