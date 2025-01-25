#Inventory Creation and Processing
from inventory import Inventory

#Create an inventory object
inventory = Inventory()

#Create a product object
from product import Product
product1 = Product("Phone", 5000, 10)
product2 = Product("Laptop", 30000, 5)
product3 = Product("Tablet", 15000, 7)
print(product1.get_details())
print(product2.get_details())
print(product3.get_details())

#Add products to inventory
inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)
print(inventory.get_details())

#Check stock of a product
product_name = input("Enter the product name to check stock: ")
print(f"Stock of {product_name}: {inventory.check_stock(product_name)}")

#Remove products from inventory
product_name = input("Enter the product name to remove: ")
quantity = int(input("Enter the quantity to remove: "))
inventory.remove_product(product_name, quantity)