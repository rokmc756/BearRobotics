#!/usr/bin/python3

# Write python3 code for a simple ATM with menu and prompt. It doesn't need any UI (either graphical or console),
# but a controller should be implemented and tested.
# Requirements should be at least the following flow should be implemented:
# Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw
# For simplification, there are only 1 dollar bills in this world, no cents. Thus account balance can be represented in integer.
# Your code doesn't need to integrate with a real bank system, but keep in mind that we may want to integrate it with a real bank system in the future.
# It doesn't have to integrate with a real cash bin in the ATM, but keep in mind that we'd want to integrate with that in the future.
# And even if we integrate it with them, we'd like to test our code.
# Implementing bank integration and ATM hardware like cash bin and card reader is not a scope of this task, but testing the controller part (not including bank system, cash bin etc) is within the scope.


class Account:
    def __init__(self, balance=1):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            return "Insufficient funds"

    def check_balance(self):
        return self.balance


class ATMController:
    def __init__(self):
        self.card_inserted = False
        self.pin_entered = False
        self.account = None

    def insert_card(self):
        self.card_inserted = True

    def enter_pin(self, pin):
        if self.card_inserted and pin == "1234":  # Assuming PIN is hardcoded for simplicity
            self.pin_entered = True
            self.account = Account()

    def select_account(self):
        if self.pin_entered:
            return self.account
        else:
            return "Please enter your PIN first"

# ATM menu
def atm_menu():
    print("ATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

# Test the ATM controller
atm_controller = ATMController()

atm_controller.insert_card()
atm_controller.enter_pin("1234")
selected_account = atm_controller.select_account()

if isinstance(selected_account, Account):
    while True:
        atm_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("Balance: $"+str(selected_account.check_balance()))
        elif choice == "2":
            amount = int(input("Enter deposit amount: $"))
            selected_account.deposit(amount)
            print(f"${amount} deposited successfully")
        elif choice == "3":
            amount = int(input("Enter withdrawal amount: $"))
            withdrawn_amount = selected_account.withdraw(amount)
            if withdrawn_amount != "Insufficient funds":
                print(f"${withdrawn_amount} withdrawn successfully")
            else:
                print("Insufficient funds")
        elif choice == "4":
            print("Exiting ATM. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print(selected_account)

