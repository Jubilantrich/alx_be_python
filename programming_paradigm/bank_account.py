# bank_account.py

class BankAccount:
    initial_balance=0.0
    def __init__(self, initial_balance):
        self._account_balance = initial_balance  # Encapsulation of account balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self._account_balance >= amount:
                self._account_balance -= amount
                return True
            else:
                return False  # Insufficient funds
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")
