#Defining the product class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    #Method to calculate the total value of products in stock
    def total_value(self):
        return self.price * self.quantity

#Creating product objects
product1 = Product("Laptop", 1000, 5)
product2 = Product("Mouse", 20, 50)


# Calculating and displaying total value
print(f"Total value of {product1.name} stock: Ghc{product1.total_value()}")
print(f"Total value of {product2.name} stock: Ghc{product2.total_value()}")