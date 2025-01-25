from product import Product
from inventory import Inventory

def main():
    inventory = Inventory()

    while True:
        print("\nWelcome to the Product Management System")
        print("1. Create a new product")
        print("2. Update an existing product")
        print("3. View product details")
        print("4. Check stock")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            # Create a new product
            name = input("Enter product name: ").strip()
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            
            new_product = Product(name, price, quantity)
            inventory.add_product(new_product)
            print(f"Product '{name}' has been added to the inventory.")

        elif choice == "2":
            # Update an existing product
            name = input("Enter the product name to update: ").strip()
            
            if name in inventory.products:
                print("What do you want to update?")
                print("1. Price")
                print("2. Quantity")
                update_choice = input("Enter your choice (1-2): ").strip()

                if update_choice == "1":
                    new_price = float(input("Enter the new price: "))
                    inventory.products[name].update_prices(new_price)
                    print(f"Price of '{name}' has been updated to Rs.{new_price}.")
                
                elif update_choice == "2":
                    new_quantity = int(input("Enter the new quantity: "))
                    inventory.products[name].update_quantity(new_quantity)
                    print(f"Quantity of '{name}' has been updated to {new_quantity}.")
                else:
                    print("Invalid choice. Please choose 1 or 2.")
            else:
                print(f"Product '{name}' not found in the inventory.")

        elif choice == "3":
            # View product details
            name = input("Enter the product name to view details: ").strip()
            if name in inventory.products:
                print(inventory.products[name].get_details())
            else:
                print(f"Product '{name}' not found in the inventory.")

        elif choice == "4":
            # Check stock
            name = input("Enter the product name to check stock: ").strip()
            stock = inventory.check_stock(name)
            print(f"Stock for '{name}': {stock} units.")

        elif choice == "5":
            # Exit
            print("Exiting the Product Management. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()
