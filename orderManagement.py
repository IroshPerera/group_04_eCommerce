#Order Creation and Processing
from order import Order

#Create a customer object
from customer import Customer
customer = Customer("John", "123 Main Street", "123456789")
print(customer.get_details())

#Create a product object
from product import Product
product1 = Product("Phone", 5000, 10)
product2 = Product("Laptop", 30000, 5)
print(product1.get_details())
print(product2.get_details())

#Create an order object
order = Order(customer, 1)
order.add_product(product1)
order.add_product(product2)
print(order.calculate_total())

