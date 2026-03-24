class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount  # use setter validation
        self.total = 0
        self.items = []
        self.previous_transactions = []

    # Property for discount
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    # Add item method
    def add_item(self, item, price, quantity):
        total_price = price * quantity
        self.total += total_price

        self.items.append(item)

        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        self.previous_transactions.append(transaction)

        print(f"Added {quantity} x {item}(s). Total is now {self.total}")

    # Apply discount method
    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        # Remove last transaction
        last_transaction = self.previous_transactions.pop()

        # Update items list
        if last_transaction["item"] in self.items:
            self.items.remove(last_transaction["item"])

        print(f"Discount applied. Total is now {self.total}")

    # Void last transaction method
    def void_last_transaction(self):
        if not self.previous_transactions:
            print("No transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()

        refund_amount = last_transaction["price"] * last_transaction["quantity"]
        self.total -= refund_amount

        # Remove item from items list
        if last_transaction["item"] in self.items:
            self.items.remove(last_transaction["item"])

        print(f"Voided last transaction. Total is now {self.total}")
        
if __name__ == "__main__":
    register = CashRegister(20)

    register.add_item("Apple", 2, 3)
    register.add_item("Banana", 1, 5)

    register.apply_discount()
    register.void_last_transaction()