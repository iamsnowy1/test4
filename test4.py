class Product:
    total_products = 0  # Статичне поле для відстеження кількості створених продуктів

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.total_products += 1

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Total products created: {Product.total_products}")

class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)
        self.warranty_period = warranty_period

    def display_info(self):
        super().display_info()
        print(f"Warranty Period: {self.warranty_period} months")

class ClothingProduct(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")

# Приклад використання класів
if __name__ == "__main__":
    # Створення продуктів різних типів
    product1 = Product("Laptop", 1200)
    electronic_product1 = ElectronicProduct("Smartphone", 800, 12)
    clothing_product1 = ClothingProduct("T-Shirt", 20, "M")

    # Виведення інформації про продукти
    print("Product 1 Info:")
    product1.display_info()
    print()

    print("Electronic Product 1 Info:")
    electronic_product1.display_info()
    print()

    print("Clothing Product 1 Info:")
    clothing_product1.display_info()
