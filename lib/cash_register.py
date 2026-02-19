#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self._discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction_amount = 0.0

    # Discount Property

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    # Add Item

    def add_item(self, item, price, quantity=1):
        transaction_total = price * quantity
        self.total += transaction_total
        self.last_transaction_amount = transaction_total

        for _ in range(quantity):
            self.items.append(item)

    # Apply Discount

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total - (self.total * self.discount / 100)

        if self.total.is_integer():
            print(
                f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print(f"After the discount, the total comes to ${self.total}.")

    # Void Last Transaction

    def void_last_transaction(self):
        self.total -= self.last_transaction_amount

        if self.total < 0:
            self.total = 0.0


# testing
register = CashRegister(20)

register.add_item("Shoes", 50, 2)
register.add_item("Hat", 20, 1)

print(register.total)

register.apply_discount()
print(register.total)

register.void_last_transaction()
print(register.total)
