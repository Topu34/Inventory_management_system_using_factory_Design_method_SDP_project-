from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

class InventoryItem(Item):
    pass

class Supplier:
    def __init__(self, supplier_id, name, email):
        self.supplier_id = supplier_id
        self.name = name
        self.email = email

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

class Invoice:
    def __init__(self, invoice_id, order_id, total_amount):
        self.invoice_id = invoice_id
        self.order_id = order_id
        self.total_amount = total_amount

class ItemFactory(ABC):
    @abstractmethod
    def create_item(self):
        pass

class ConcreteFactory(ItemFactory):
    def create_item(self, code, name, price):
        return InventoryItem(code, name, price)

class ConcreteSupplierFactory(ItemFactory):
    def create_item(self, supplier_id, name, email):
        return Supplier(supplier_id, name, email)

class ConcreteOrderFactory(ItemFactory):
    def create_item(self, order_id, items):
        return Order(order_id, items)

class ConcreteInvoiceFactory(ItemFactory):
    def create_item(self, invoice_id, order_id, total_amount):
        return Invoice(invoice_id, order_id, total_amount)

class Inventory:
    def __init__(self):
        self.items = {}
        self.suppliers = {}
        self.orders = []  

    def add_item(self, item, quantity):
        if item.code in self.items:
            self.items[item.code]['quantity'] += quantity
        else:
            self.items[item.code] = {'item': item, 'quantity': quantity}

    def remove_item(self, item_code, quantity):
        if item_code in self.items:
            if quantity <= self.items[item_code]['quantity']:  
                self.items[item_code]['quantity'] -= quantity
                if self.items[item_code]['quantity'] <= 0:
                    del self.items[item_code]
                print("Item removed successfully!")
            else:
                print("Insufficient quantity to remove.")
        else:
            print("Item not found in inventory!")

    def get_item_details(self, item_code):
        item_data = self.items.get(item_code)
        if item_data:
            item = item_data['item']
            return {'code': item.code, 'name': item.name, 'price': item.price, 'quantity': item_data['quantity']}
        else:
            return None

    def place_order(self, order):
        self.orders.append(order)  
        print("Order placed successfully!")

    def update_inventory(self, order):     
        for item in order.items:
            self.add_item(item['item'], -item['quantity'])  

    def generate_invoice(self, order):
        
        total_amount = sum(item['item'].price * item['quantity'] for item in order.items)
        invoice_id = len(self.orders)  
        invoice = Invoice(invoice_id, order.order_id, total_amount)
        return invoice

    def add_supplier(self, supplier):
        self.suppliers[supplier.supplier_id] = supplier

    def update_supplier(self, supplier):
        if supplier.supplier_id in self.suppliers:
            self.suppliers[supplier.supplier_id] = supplier

    def track_supplier_price(self, supplier_id, item_code):
        
        pass

def authenticate_user():
    users = {'admin': 'admin123'}
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username] == password:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password. Please try again.")

def main():
    if authenticate_user():
        factory = ConcreteFactory()
        supplier_factory = ConcreteSupplierFactory()
        order_factory = ConcreteOrderFactory()
        invoice_factory = ConcreteInvoiceFactory()
        inventory = Inventory()

        while True:
            print("\nInventory Management System")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. Get Item Details")
            print("4. Place Order")
            print("5. Add Supplier")
            print("6. Update Supplier")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                code = input("Enter item code: ")
                name = input("Enter item name: ")
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                item = factory.create_item(code, name, price)
                inventory.add_item(item, quantity)
                print("Item added successfully!")
            
            elif choice == '2':
                code = input("Enter item code to remove: ")
                quantity = int(input("Enter quantity to remove: "))
                inventory.remove_item(code, quantity)
            elif choice == '3':
                code = input("Enter item code to get details: ")
                item_details = inventory.get_item_details(code)
                if item_details:
                    print(f"Item Details: Code - {item_details['code']}, Name - {item_details['name']}, "
                          f"Price - ${item_details['price']}, Quantity - {item_details['quantity']}")
                else:
                    print("Item not found in inventory.")
            
            elif choice == '4':
                print("Placing order...")
                order_items
                order_items = []
                while True:
                    item_code = input("Enter item code to order (or 'done' to finish): ")
                    if item_code.lower() == 'done':
                        break
                    quantity = int(input("Enter quantity to order: "))
                    item_data = inventory.get_item_details(item_code)
                    if item_data:
                        item = item_data['item']
                        if quantity <= item_data['quantity']:
                            order_items.append({'item': item, 'quantity': quantity})
                            print(f"{quantity} {item.name}(s) added to the order.")
                        else:
                            print("Insufficient quantity in inventory.")
                    else:
                        print("Item not found in inventory.")
                
                if order_items:
                    order_id = len(inventory.orders) + 1
                    order = order_factory.create_item(order_id, order_items)
                    inventory.place_order(order)
                    inventory.update_inventory(order)
                    print("Order placed successfully!")
                else:
                    print("No items added to the order.")
            
            elif choice == '5':
                supplier_id = int(input("Enter supplier ID: "))
                name = input("Enter supplier name: ")
                email = input("Enter supplier email: ")
                supplier = supplier_factory.create_item(supplier_id, name, email)
                inventory.add_supplier(supplier)
                print("Supplier added successfully!")
            
            elif choice == '6':
                supplier_id = int(input("Enter supplier ID to update: "))
                name = input("Enter updated supplier name: ")
                email = input("Enter updated supplier email: ")
                supplier = Supplier(supplier_id, name, email)
                inventory.update_supplier(supplier)
                print("Supplier updated successfully!")

            elif choice == '7':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()







