# Implement Your Own Data Structures
class CustomDat():
    def __init__(self):
        self.inventory = {
            "apple": (10, 2.5),
            "mango": (2, 5.0)
        }

    def add_update_item(self, item: str, quantity: int, price: float):
        if item in self.inventory:
            print(f"Updating info of {item} with quantity of {quantity} and price of {price}")
        else:
            print(f"Adding {item} with quantity of {quantity} and price of {price}")

        self.inventory[item] = (quantity, price)

    
    def remove_item(self, item: str):
        if not self.inventory.pop(item, None):
            print(f"{item} not found! Nothing removed")
        else:
            print(f"Successfully removed {item}")
        

    def display(self):
        for item, info in self.inventory.items():
            print(f"Item: {item}, Quantity: {info[0]}, Price: ${info[1]}")


datastruct = CustomDat()
datastruct.add_update_item("strawberry", 100, 1.0)
datastruct.add_update_item("strawberry", 40, 1.0)
datastruct.display()
datastruct.remove_item("strawberry")
datastruct.display()

""" Adding strawberry with quantity of 100 and price of 1.0
Updating info of strawberry with quantity of 40 and price of 1.0
Item: apple, Quantity: 10, Price: $2.5
Item: mango, Quantity: 2, Price: $5.0
Item: strawberry, Quantity: 40, Price: $1.0
Successfully removed strawberry
Item: apple, Quantity: 10, Price: $2.5
Item: mango, Quantity: 2, Price: $5.0 """