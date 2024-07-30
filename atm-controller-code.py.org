#!/usr/bin/python3

class Account:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

class ATM:
    def __init__(self):
        self.current_account = None

    def insert_card(self):
        account_number = input("Please enter your account number: ")
        pin = input("Please enter your PIN: ")

        # In a real scenario, here we would connect to a bank API to verify the account number and pin
        # For simplicity, we'll just hardcode one account for demonstration purposes
        if account_number == '751008' and pin == '1234':
            self.current_account = Account(account_number, pin, 1000)
            return True
        else:
            return False

    def select_account(self):
        if self.current_account:
            return self.current_account
        else:
            return None

    def check_balance(self):
        if self.current_account:
            return self.current_account.balance
        else:
            return None

    def deposit(self, amount):
        if self.current_account:
            self.current_account.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if self.current_account and self.current_account.balance >= amount:
            self.current_account.balance -= amount
            return True
        else:
            return False

# Testing the ATM controller
atm = ATM()

# Insert Card
if atm.insert_card():
    print("Card inserted successfully")
else:
    print("Invalid account number or pin")

# Select Account
selected_account = atm.select_account()
if selected_account:
    print(f"Selected Account Number: {selected_account.account_number}")

    # Check Balance
    balance = atm.check_balance()
    print(f"Current Balance: ${balance}")

    # Deposit
    deposit_amount = int(input("Enter the amount to deposit: $"))
    if atm.deposit(deposit_amount):
        print(f"Deposited ${deposit_amount} successfully")
    else:
        print("Deposit failed")

    # Withdraw
    withdraw_amount = int(input("Enter the amount to withdraw: $"))
    if atm.withdraw(withdraw_amount):
        print(f"Withdrew ${withdraw_amount} successfully")
    else:
        print("Withdrawal failed")

    # Check Balance after transactions
    balance = atm.check_balance()
    print(f"Current Balance: ${balance}")
else:
    print("Error: Account not selected")
