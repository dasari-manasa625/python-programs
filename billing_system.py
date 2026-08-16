class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class Bill:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.total_price()
        return total

    def display_bill(self):
        print("\n--------- BILL ---------")
        print("Product\tPrice\tQuantity\tTotal")

        for product in self.products:
            print(
                product.name,
                "\t",
                product.price,
                "\t",
                product.quantity,
                "\t\t",
                product.total_price()
            )

        subtotal = self.calculate_total()
        tax = subtotal * 0.05
        final_total = subtotal + tax

        print("------------------------")
        print("Subtotal:", subtotal)
        print("Tax (5%):", tax)
        print("Final Total:", final_total)


# Create products
product1 = Product("Pen", 10, 2)
product2 = Product("Notebook", 50, 3)
product3 = Product("Pencil", 5, 4)

# Create bill
bill = Bill()

# Add products
bill.add_product(product1)
bill.add_product(product2)
bill.add_product(product3)

# Display bill
bill.display_bill()