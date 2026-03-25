class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        total_price = price * quantity
        self.total += total_price

        for _ in range(quantity):
            self.items.append(item)

        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        self.previous_transactions.append(transaction)

        print(f"Added {quantity} x {item}(s). Total is now {self.total}")

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        print(f"Discount applied. Total is now {self.total}")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("No transaction to void.")
            return

        last_transaction = self.previous_transactions.pop()

        refund_amount = last_transaction["price"] * last_transaction["quantity"]
        self.total -= refund_amount

        for _ in range(last_transaction["quantity"]):
            if last_transaction["item"] in self.items:
                self.items.remove(last_transaction["item"])

        print(f"Voided last transaction. Total is now {self.total}")
        
if __name__ == "__main__":
    register = CashRegister(20)

    register.add_item("Apple", 2, 3)
    register.add_item("Banana", 1, 5)

    register.apply_discount()
    register.void_last_transaction()