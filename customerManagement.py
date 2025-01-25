from customer import Customer

class CustomerManagement:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        if customer.name in self.customers:
            print(f"Customer '{customer.name}' already exists.")
        else:
            self.customers[customer.name] = customer
            print(f"Customer '{customer.name}' has been added successfully.")

    def view_customer_details(self, name):
        if name in self.customers:
            print(self.customers[name].get_details())
        else:
            print(f"Customer '{name}' not found.")


def main():
    management = CustomerManagement()

    while True:
        print("\nCustomer Management System")
        print("1. Add a new customer")
        print("2. View customer details")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            # Add a new customer
            name = input("Enter customer's name: ").strip()
            address = input("Enter customer's address: ").strip()
            contact = input("Enter customer's contact number: ").strip()

            new_customer = Customer(name, address, contact)
            management.add_customer(new_customer)

        elif choice == "2":
            # View customer details
            name = input("Enter the customer's name to view details: ").strip()
            management.view_customer_details(name)

        elif choice == "3":
            # Exit
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


main()